/*----------------------------------------------------------
V0.3.4
--------------------------------------------------------*/

#include <lzFreeRTOS.h> 
#include <Keypad.h>
#include <Stepper.h>
#include <Adafruit_SSD1306.h>

//-----------------------初始化-------------------------------
//---------输入键盘---------------

const byte ROWS = 4; //four rows
const byte COLS = 4; //four columns
//define the cymbols on the buttons of the keypads
char hexaKeys[ROWS][COLS] = {
{'4','K','2','U'},
{'3','k','F','D'},
{'2','9','O','u'},
{'1','D','E','d'}
};
//connect to the row pinouts of the keypad
//R1,R2,R3
byte rowPins[ROWS] = {6, 7, 8, 9}; 
//connect to the column pinouts of the keypad
byte colPins[COLS] = {5, 4, 3, 2}; 
//initialize an instance of class NewKeypad
Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);

//-----------输出步进电机-------------------

const int STEPS_PER_ROTOR_REV = 32; 
//  减速比
const int GEAR_REDUCTION = 64;
const float STEPS_PER_OUT_REV = STEPS_PER_ROTOR_REV * GEAR_REDUCTION;
// 电机旋转步数
Stepper steppermotor(STEPS_PER_ROTOR_REV, 31, 29, 30, 28); 
//------------OLED显示屏-----------------------------
//Adafruit_SSD1306 display(4);


//------------全局变量（运行状态）----------------
int now_h=1;
int wait_in=0,plan_to[5]={0};
int wait[5][2]={0};
int to[5]={0};
int time=0;
int reward=0,work=0;
int up=0,down=0;
char customKey;
//-----------工作函数----------------------------
void serial_print(){
	Serial.print(now_h);
	for(int i=1;i<=4;i++){
		if(i!=4)Serial.print(wait[i][1]);
		if(i!=1)Serial.print(wait[i][0]);
		Serial.print(plan_to[i]);
	}
	Serial.print(reward);
	Serial.print('\n');
}

int reward_calculation(){
	int _reward=0;
	for(int i=0;i<5;i++){
		_cost+=abs(now_h-i)*wait[i][0];
		_cost+=abs(now_h-i)*wait[i][0];
		_cost+=(abs(now_h-i)*plan_to[i]*2);
	}
	return _cost;
}

void moving(int _how){
	if(_how==0){
		if(now_h!=4){
			steppermotor.step(3900);
			now_h++;
		}
		else{
			vTaskDelay(20);
		}
	}
	else if(_how==1){
		if(now_h!=1){
			steppermotor.step(-3900);
			now_h--;
		}
		else{
			vTaskDelay(20);
		}
	}
	else{
		vTaskDelay(2000);
	}
}

//---------------------------------------------

/**
 * 任务1：接受按键数据
 */
void v_get_key_Task(void *pvParameters){
    while(1){
		customKey = customKeypad.getKey();
		if(customKey=='F'){
			wait[4][0]=1;
		}
		else if(customKey=='O'){
			wait[1][1]=1;
		}
		else if(customKey=='u'){
			wait[2][1]=1;
		}
		else if(customKey=='d'){
			wait[2][0]=1;
		}
		else if(customKey=='U'){
			wait[3][1]=1;
		}
		else if(customKey=='D'){
			wait[3][0]=1;
		}
		else if(customKey=='1'){
			plan_to[1]=1;
		}
		else if(customKey=='2'){
			plan_to[2]=1;
		}
		else if(customKey=='3'){
			plan_to[3]=1;
		}
		else if(customKey=='4'){
			plan_to[4]=1;
		}
		else if(customKey=='K'){
			steppermotor.step(3900);
		}
		else if(customKey=='k'){
			steppermotor.step(-3900);
		}
	}
	
}

/**
 * 任务2：控制步进电机与显示
 */
void v_moving_Task(void *pvParameters){
	pinMode(LED_BUILTIN, OUTPUT);
//	display.begin(SSD1306_SWITCHCAPVCC, 0x3C); 
	Serial.begin(9600);
    steppermotor.setSpeed(1100); 
    while(1){
		vTaskDelay(100);
		reward = reward_calculation();
		serial_print();
		if(Serial.available()){
			work=Serial.read();
			moving(work);
		}
	}
}
/**
 * 任务3：判断&修改数据
 */
void v_check_Task(void *pvParameters){
	while(1){
		vTaskDelay(50);
		if((wait[now_h][0] or wait[now_h][1]) and work==3){
			wait[now_h][0]=wait[now_h][1]=0;
		}
		if(work==3 and plan_to[now_h])plan_to[now_h]=0;
	}
}

void setup(){
    //创建任务1
    xTaskCreate(v_get_key_Task,//任务函数
                "Task1",     //任务名称
                64,//任务堆栈大小
                NULL,       //任务函数参数传递
                2,//优先级
                NULL);//任务句柄

    //创建任务2
    xTaskCreate(v_moving_Task,
                "Task2",
                64,
                NULL,
                2,
                NULL);
	//任务3
	xTaskCreate(v_check_Task,
                "Task3",
                64,
                NULL,
                2,
                NULL);
    //任务调度
    vTaskStartScheduler();
}

void loop(){
    
}

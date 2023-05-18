

#include <ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <sensor_msgs/JointState.h>
#include <Servo.h>
#include <LiquidCrystal_I2C.h>
#define PI 3.1415926535897932384626433832795

#define MAP(_val, _oldL, _oldH, _newL, _newH)	( ((double)_newH - _newL)*((double)_val - _oldL)/( (double)_oldH - _oldL) + _newL )


// float servosVals_LowOld[  12] = {0};
// float servosVals_HighOld[ 12] = {0};
// float servosVals_LowNew[  12] = {0};
// float servosVals_HighNew[ 12] = {0};

float servosVals[12] = {0};
LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C address 0x27, 16 column and 2 rows
ros::NodeHandle nh;

float global_cur_pos[12] = {0};
int servosPins[12] = {44, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2};

Servo servos[12];
int servoPins[12] = {13, 12, 11,     10,  9,   8,      7,  6,  5,       4,  3,   2};
int offset[12]    = {90, 90, 45,     90, 90, 135,     90, 90, 45,      90, 45, 135};
int dir[12]       = {-1, -1, -1,      1,  1,   1,      1,  1,  1,      -1,  1,   1};


void jointStateCallback(const std_msgs::Float32MultiArray& msg)
{
  const int num_joints = 12;
  for (int i = 0; i < num_joints; i++)
  {
    servos[i].write((int)((msg.data[i]*(180.0/3.14)*dir[i])  + offset[i]));
  }
}

ros::Subscriber<std_msgs::Float32MultiArray> sub("test_a_topic", &jointStateCallback);

void setup()
{
  servos[0] .write(90);
  servos[1] .write(90);
  servos[2] .write(45);

  servos[3] .write(90);
  servos[4] .write(90);
  servos[5] .write(135);

  servos[6] .write(90);
  servos[7] .write(90);
  servos[8] .write(45);

  servos[9] .write(90);
  servos[10].write(45);
  servos[11].write(135);
    
  nh.getHardware()->setBaud(115200);
  nh.initNode();
  nh.subscribe(sub);

  for (int i = 0; i < 12; i++)
  {
    servos[i].attach(servoPins[i]); // Attach servos to pins 2 to 13
    
  }
}

void loop()
{
  nh.spinOnce();
}
















// marawan:
/*
#include <ros.h>
#include <sensor_msgs/JointState.h>
#include <Servo.h>
#include <LiquidCrystal_I2C.h>


LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C address 0x27, 16 column and 2 rows

ros::NodeHandle nh;

float global_cur_pos[12] = {0};  // Changed data type to float

void jointStateCallback(const sensor_msgs::JointState& joint_state_msg)
{
  lcd.print("hi");
  const int num_joints = 12; 

  for (int i = 0; i < num_joints; i++)
  {
    int new_pos = static_cast<int>(joint_state_msg.position[i]);  
    
    lcd.setCursor(i*4, 1);
    lcd.print(new_pos);
    

    

  }
}

ros::Subscriber<sensor_msgs::JointState> sub("joint_states", jointStateCallback);

void setup()
{
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Ard. ");


  nh.getHardware()->setBaud(115200);
  nh.initNode();
  nh.subscribe(sub);

  
}

void loop()
{
  nh.spinOnce();
}

*/












/*

#include <ros.h>
#include <sensor_msgs/JointState.h>
#include <std_msgs/Float32.h>
#include <rospy_tutorials/Floats.h>


#include <Servo.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C address 0x27, 16 column and 2 rows

ros::NodeHandle nh;


void callback(const sensor_msgs::JointState &msg) {
  // float value = msg.position[0];
  // lcd.setCursor(0, 1);
  // lcd.print(value);


  for (int i = 0; i < msg.position_length; i++)
  {
    lcd.setCursor(i*8,1);
    lcd.print("J.");    lcd.print(i);    lcd.print(": ");    lcd.print(msg.position[i]);
  }
  
  
}

ros::Subscriber<sensor_msgs::JointState> sub("joint_states", &callback);    // then test / before topic name



void setup() {
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Ard. ");

  nh.getHardware()->setBaud(115200);
  nh.initNode();
  nh.subscribe(sub);

}



void loop() {
  nh.spinOnce();
}

*/













/*

#include <ros.h>
#include <sensor_msgs/JointState.h>
#include <std_msgs/Float32.h>
#include <rospy_tutorials/Floats.h>


#include <Servo.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

ros::NodeHandle nh;


void callback(const std_msgs::Float32 &msg) {
  float value = msg.data;

  lcd.setCursor(0, 1);
  lcd.print((float)value);
  
  
}

ros::Subscriber<std_msgs::Float32> sub("test_a_topic", &callback);    // then test / before topic name



void setup() {
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Ard. ");

  nh.getHardware()->setBaud(115200);
  nh.initNode();
  nh.subscribe(sub);
}



void loop() {
  nh.spinOnce();
}
*/

















/*
#include <ros.h>
#include <sensor_msgs/JointState.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Float64.h>
#include <rospy_tutorials/Floats.h>

#include <Servo.h>
#include <LiquidCrystal_I2C.h>



LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C address 0x27, 16 column and 2 rows



ros::NodeHandle nh;



// void jointStatesCallback(const sensor_msgs::JointState& msg)
void jointStatesCallback(const std_msgs::Float64& msg)
{
  for (int i = 0; i < msg.position_length-10; i++)
  {
    lcd.setCursor(i*8,1);
    lcd.print("J.");    lcd.print(i);    lcd.print(": ");    lcd.print(msg.data);
    // lcd.print("J.");    lcd.print(i);    lcd.print(": ");    lcd.print(msg.position[i]);
  }
}

ros::Subscriber<sensor_msgs::JointState> sub("joint_states", &jointStatesCallback, 1000);

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Ard. ");


  nh.getHardware()->setBaud(115200);
  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  // delay(1);
}

*/














/*
#include <ros.h>
#include <rospy_tutorials/Floats.h>
#include <Servo.h>

ros::NodeHandle nh;

int global_cur_pos[12] = {0};

Servo servos[12];

void setup()
{
  nh.initNode();
  nh.subscribe("/joints_to_arduino", &servo_cb);

  for (int i = 0; i < 12; i++)
  {
    servos[i].attach(i + 2); // Attach servos to pins 2 to 13
    servos[i].write(90);     // Initialize servos to position 90
  }
}



void loop()
{
  
  nh.spinOnce();

}




void servo_cb(const rospy_tutorials::Floats &cmd_msg)
{
  int new_pos[12] = {0};
  for (int i = 0; i < 12; i++)
  {
    new_pos[i] = cmd_msg.data[i];
    rotate_servo(i, new_pos[i], global_cur_pos[i], 1);
  }
}




void rotate_servo(int servo, int new_pos, int cur_pos, int dir)
{
  int pos = 0;

  if (new_pos < 0)
    new_pos = 0;
  else if (new_pos > 180)
    new_pos = 180;

  if (dir == 1)
  {
    for (pos = cur_pos; pos <= new_pos; pos += 1)
    {
      servos[servo].write(pos);
      delay(10);
    }
  }
  else if (dir == -1)
  {
    for (pos = cur_pos; pos >= new_pos; pos -= 1)
    {
      servos[servo].write(pos);
      delay(10);
    }
  }

  global_cur_pos[servo] = pos;
}

*/









/*

#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle  nh;

std_msgs::String str_msg;
ros::Publisher chatter("chatter", &str_msg);

char hello[13] = "hello world!";

void setup()
{
  nh.initNode();
  nh.advertise(chatter);
}

void loop()
{
  str_msg.data = hello;
  chatter.publish( &str_msg );
  nh.spinOnce();
  delay(1000);
}

*/

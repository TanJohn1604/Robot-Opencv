
#include <Servo.h>

#define numOfValsRec 4
#define digitsPerValRec 3
int valsRec[numOfValsRec];
int stringLength=numOfValsRec*digitsPerValRec+1;
int counter =0;
bool counterStart=false;
String receivedString;
int lowtemp=0;
int hightemp=0;
int homeflag=0;
Servo myservo[4];
const int SERVOS = 4;
int currentAngle[SERVOS], MIN[SERVOS], MAX[SERVOS], INITANGLE[SERVOS],PIN[4] ;
int Analog[4];
int buttonState = 0;   
void setup() {
  PIN[0] = 6;                   
  MIN[0] = 0;                  //góc min
  MAX[0] = 180;                 //góc Max
  INITANGLE[0] = 90;      //ĐÂY LÀ GÓC BAN ĐẦU Servo base
  
  PIN[1] = 9;                   //Chân nối Servo
  MIN[1] = 120;                  //góc min
  MAX[1] = 180;                //góc Max
  INITANGLE[1] = 120;           //ĐÂY LÀ GÓC BAN ĐẦU servo nang
  
  PIN[2] = 10;                 //Chân nối Servo
  MIN[2] = 100;                 //góc min
  MAX[2] = 140;                //góc Max
  INITANGLE[2] = 100;           // ĐÂY LÀ GÓC BAN ĐẦU servo high

  PIN[3] = 11;                 //Chân nối Servo
  MIN[3] = 100;                 //góc min
  MAX[3] = 137;                //góc Max
  INITANGLE[3] = 100;           // ĐÂY LÀ GÓC BAN ĐẦU servo kep

  for (int i = 0; i < SERVOS; i++){
    myservo[i].attach(PIN[i]);
    myservo[i].write(INITANGLE[i]);
    
    currentAngle[i]=INITANGLE[i];
    valsRec[i]=INITANGLE[i];
  }

pinMode(A0, INPUT);
pinMode(A1, INPUT);
pinMode(A2, INPUT);
pinMode(A3, INPUT);

pinMode(2, INPUT);

Serial.begin(9600);
pinMode(LED_BUILTIN, OUTPUT);

}

int ServoMode_1(Servo myservo,int currenta,int temp, int Min,int Max){
  if(temp ==0){
    currenta--;
    if(currenta<Min){
      currenta=Min;
    }
    
     myservo.write(currenta);  
    delay(15);  
  }
  if(temp ==1023){
    currenta++;
    if(currenta>Max){
      currenta=Max;
    }
     myservo.write(currenta);              
    delay(15);  
  }
  return currenta;
}

void receiveData(){
  while (Serial.available()){
    char c = Serial.read();
    if (c=='$'){
      counterStart=true;
    }
    if (counterStart){
      if(counter<stringLength){
        receivedString=String(receivedString+c);
      counter++;
      }
      if(counter>=stringLength){
       for (int i=0;i<numOfValsRec;i++){
        int num=(i*digitsPerValRec)+1;
        valsRec[i]=receivedString.substring(num,num+digitsPerValRec).toInt();
       }
       receivedString="";
       counter=0;
       counterStart=false;
      }
    }
    
  }

  for (int i=0;i<4;i++){
    if(valsRec[i]<MIN[i]){
      valsRec[i]=MIN[i];
    }
    if(valsRec[i]>MAX[i]){
      valsRec[i]=MAX[i];
    }
  }
  
}

void ServoMode_2(){
  for(int i=0;i<4;i++){
    while(currentAngle[i] != valsRec[i]){
      if(currentAngle[i] < valsRec[i]){
        myservo[i].write(currentAngle[i]++);
      delay(15);
      }
      if(currentAngle[i] > valsRec[i]){
        myservo[i].write(currentAngle[i]--);
      delay(15);
      }
      
    }
    myservo[i].write(currentAngle[i]);
  }
  
  
}


void loop() {

buttonState = digitalRead(2);

if(buttonState==LOW){
  
  if(homeflag==0){
    for (int i = 0; i < SERVOS; i++){
valsRec[i]=INITANGLE[i];
   ServoMode_2();
  }
  homeflag=1;
  }
  lowtemp++;

  if(lowtemp >500){
    lowtemp==501;
    hightemp=0;
    Analog[0]=analogRead(A0);
Analog[1]=analogRead(A1);
Analog[2]=analogRead(A2);  
Analog[3]=analogRead(A3);
for(int i =0 ;i<4;i++){
  currentAngle[i]=ServoMode_1(myservo[i],currentAngle[i],Analog[i],MIN[i],MAX[i]);
};
  }
  

}

if(buttonState==HIGH){
  hightemp++;

  if(homeflag==1){
    for (int i = 0; i < SERVOS; i++){
valsRec[i]=INITANGLE[i];
   ServoMode_2();
  }
  homeflag=0;
  }
  if(hightemp>500){
   hightemp=501;
   lowtemp=0;
  receiveData();
ServoMode_2();
  }
 

}




  }

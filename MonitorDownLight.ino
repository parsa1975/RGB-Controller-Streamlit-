void setup(){
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
  digitalWrite(4,HIGH);
  Serial.begin(9600);
}
void loop(){
  if (Serial.available()){
    String value = Serial.readStringUntil('\n');
    if (value == "rh"){
      digitalWrite(2,LOW);
    }
    else if (value == "rl"){
      digitalWrite(2,HIGH);
    }
    else if (value == "gh"){
      digitalWrite(3,LOW);
    }
    else if (value == "gl"){
      digitalWrite(3,HIGH);
    }
    else if (value == "bh"){
      digitalWrite(4,LOW);
    }
    else if (value == "bl"){
      digitalWrite(4,HIGH);
    }
  }
}

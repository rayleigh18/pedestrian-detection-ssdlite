#define PIN_LED A5
#define PIN_BUZZER A1
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_BUZZER, OUTPUT);
}
int val = 0;
unsigned long time = 0;
bool dataBuzz = 0;

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    val = char(Serial.read()) - '0';
    Serial.write("\n");
    digitalWrite(LED_BUILTIN, val);
    digitalWrite(PIN_LED, val);
//    digitalWrite(PIN_BUZZER, val);
    if (val){
      tone(PIN_BUZZER, 1000);
    }
    else{
      noTone(PIN_BUZZER);
    }
      
  }
}

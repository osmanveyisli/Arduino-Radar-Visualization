#include <Stepper.h>

const int STEPS_PER_REVOLUTION = 2048;

// ULN2003 driver pins
const int IN1 = 8;
const int IN2 = 9;
const int IN3 = 10;
const int IN4 = 11;

// HC-SR04 pins
const int TRIG_PIN = 6;
const int ECHO_PIN = 7;

const int MIN_ANGLE = 0;
const int MAX_ANGLE = 180;
const int ANGLE_STEP = 2;

Stepper radarMotor(
  STEPS_PER_REVOLUTION,
  IN1,
  IN3,
  IN2,
  IN4
);

int currentAngle = 0;

long angleToSteps(int angleChange) {
  return (long) angleChange * STEPS_PER_REVOLUTION / 360;
}

int measureDistanceCm() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  unsigned long duration = pulseIn(ECHO_PIN, HIGH, 30000);

  if (duration == 0) {
    return 0;
  }

  return duration * 0.0343 / 2;
}

void moveToAngle(int targetAngle) {
  int angleChange = targetAngle - currentAngle;
  long steps = angleToSteps(angleChange);

  radarMotor.step(steps);
  currentAngle = targetAngle;
}

void sendMeasurement(int angle) {
  moveToAngle(angle);
  delay(40);

  int distance = measureDistanceCm();

  Serial.print(angle);
  Serial.print(",");
  Serial.println(distance);
}

void setup() {
  Serial.begin(9600);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  radarMotor.setSpeed(10);

  // The sensor must be manually positioned at 0° before startup.
  currentAngle = 0;

  delay(1000);
}

void loop() {
  for (int angle = MIN_ANGLE; angle <= MAX_ANGLE; angle += ANGLE_STEP) {
    sendMeasurement(angle);
  }

  for (int angle = MAX_ANGLE; angle >= MIN_ANGLE; angle -= ANGLE_STEP) {
    sendMeasurement(angle);
  }
}

from machine import Pin, PWM, ADC
adc = machine.ADC(27)
pwm0 = PWM(Pin(21))      
pwm0.freq(1000)         
while True:
    digital_value = adc.read_u16() 
    pwm0.duty_u16(digital_value)  
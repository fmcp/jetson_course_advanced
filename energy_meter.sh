#Energy

#Whole board
watch -n 0,1 cat /sys/bus/i2c/drivers/ina3221x/6-0040/iio:device0/in_current0_input

#GPU
watch -n 0,1 cat /sys/bus/i2c/drivers/ina3221x/6-0040/iio:device0/in_current1_input

#CPU
watch -n 0,1 cat /sys/bus/i2c/drivers/ina3221x/6-0040/iio:device0/in_current2_input

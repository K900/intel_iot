# Краткая справка по возможностям каждой платы (с точностью до ноги):

### Большая плата Intel Edison Arduino Board:

* 0: GPIO
* 1: GPIO
* 2: GPIO
* 3: GPIO, ШИМ
* 4: GPIO
* 5: GPIO, ШИМ
* 6: GPIO, ШИМ
* 7: GPIO
* 8: GPIO
* 9: GPIO, ШИМ
* 10: GPIO, ШИМ
* 11: GPIO, ШИМ
* 12: GPIO
* 13: GPIO
* 14: GPIO, ЦАП
* 15: GPIO, ЦАП
* 16: GPIO, ЦАП
* 17: GPIO, ЦАП
* 18: GPIO, ЦАП, I2C
* 19: GPIO, ЦАП, I2C

*Важное замечание*: для работы ЦАПов 10-13 пины переключаются на ввод.

*Полезная информация*: при режиме работы GPIO_IN возвращается объект класса `EdisonArduinoGpioIn`, а не стандартный
`GpioIn`. Отличие заключается в наличии свойства `pullup`, которое управляет подключением/отключением встроенных
в плату подтягивающих резисторов.

### Маленькая плата Intel Edison Mini Breakout Board:

Имена контактов приводятся соответственно официальной маркировке.
Для настройки контакта передаем его имя в виде строки.

* J17-1: GPIO, ШИМ
* J17-5: GPIO
* J17-7: GPIO, I2C
* J17-8: GPIO
* J17-9: GPIO, I2C
* J17-10: GPIO
* J17-11: GPIO
* J17-12: GPIO
* J17-14: GPIO
* J18-1: GPIO, ШИМ
* J18-2: GPIO
* J18-6: GPIO
* J18-7: GPIO, ШИМ
* J18-8: GPIO, ШИМ
* J18-10: GPIO
* J18-11: GPIO
* J18-12: GPIO
* J18-13: GPIO
* J19-4: GPIO
* J19-5: GPIO
* J19-6: GPIO
* J19-8: GPIO
* J19-9: GPIO
* J19-10: GPIO
* J19-11: GPIO
* J19-12: GPIO
* J19-13: GPIO
* J19-14: GPIO
* J20-4: GPIO
* J20-5: GPIO
* J20-6: GPIO
* J20-7: GPIO
* J20-8: GPIO
* J20-9: GPIO
* J20-10: GPIO
* J20-11: GPIO
* J20-12: GPIO
* J20-13: GPIO
* J20-14: GPIO
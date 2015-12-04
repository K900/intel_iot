# Главное
* запускаем скрипты от `sudo`: `sudo python3 имя_файла.py`.
    * все ошибки про permission denied вызваны именно этим

* для большой платы модуль - `intel_iot.board.edison.arduino`, для маленькой - `intel_iot.board.edison.mini`
* самый нормальный способ подключить - `import *`

```python
from intel_iot.board.edison.arduino import *
pin = board.setup(1, GPIO_OUT)
```

# Большая плата
* номера ног - 0, 1, 2, 3, ..., 18. Для АЦП есть константы A0-A7
* 7 ногу лучше не трогать, происходят странные вещи с Wi-Fi

# Маленькие платы
* номера ног - "J17-1" - "J17-13", "J18-1" - "J18-13" ... "J20-13" (строками!)
* уровень сигнала на выходе - 1.8В, для управления почти всем нужно делать ключ на транзисторе

# Цифровой ввод
* `pin = board.setup(x, GPIO_IN)`
* читаем из `pin.value`

# Цифровой вывод
* `pin = board.setup(x, GPIO_OUT)`
* пишем 0/1 в `pin.value`
* доступ к `pin.value` дает последнее записанное значение (в том числе от других процессов!)

# ШИМ
* `pin = board.setup(x, PWM)`
* период в `pin.period` (наносекунды), время высокого уровня в течение периода в `pin.duty_cycle` (тоже наносекунды)
* включаем `pin.enabled = True`
* [Википедия](https://ru.wikipedia.org/wiki/%D0%A8%D0%98%D0%9C)

# АЦП (только большая плата)
* `pin = board.setup(x, ADC)`
* читаем из `pin.value`
* разрешение АЦП - 10 бит

# I2C (WIP)
* `bus = board.setup(18, I2C)`
* на больших платах одна шина, на маленьких - две
* прогается через [smbus-cffi](https://github.com/bivab/smbus-cffi)
    * исходники сабжа с документацией [тут](https://github.com/bivab/smbus-cffi/blob/master/smbus/smbus.py)

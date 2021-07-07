class SemaphoreFlagsDecoder():
    """ Работаем с семафорной азбукой
    Методы:
        getSemaphoreRu(str)
        getSemaphoreEn(str)
    """

    def __init__(self):
        self.semaphoreRu = {
            'н-н': ' ',
            'лн-пн': 'а',
            'л-лн': 'б',
            'л-н': 'в',
            'н-п': 'г',
            'пн-п': 'д',
            'лв-н': 'е',
            'лв-п': 'ж',
            'л-пв': 'з',
            'в-н': 'и',
            'пн-пв': 'к',
            'лв-пн': 'л',
            'лн-пв': 'м',
            'лн-н': 'н',
            'н-пн': 'о',
            'в-п': 'п',
            'л-в': 'р',
            'н-пв': 'с',
            'л-п': 'т',
            'лв-пв': 'у',
            'в-пн': 'ф',
            'лв-лн': 'х',
            'л-пн': 'ц',
            'лн-п': 'ч',
            'в-пв': 'ш',
            'лв-в': 'щ',
            'в-в': 'ь',
            'лн-в': 'ы',
            'лв-л': 'ю',
            'п-пв': 'я',
        }
        self.semaphoreEn = {
            'н-н': ' ',
            'в-п':'_letters',
            'в-пв':'_numbers',
            'лн-н': 'a',
            'л-н': 'b',
        }
        # добавляем ключи с обратным написанием: нл-нп
        for key, value in list(self.semaphoreRu.items()): # создаем копию словаря, чтобы добавлять элементы
            if len(key) > 3: # короткие ключи не поворачиваем
                self.semaphoreRu[key.split('-')[0][::-1] + '-' + key.split('-')[1][::-1]] = value
        for key, value in list(self.semaphoreEn.items()): # создаем копию словаря, чтобы добавлять элементы
            if len(key) > 3: # короткие ключи не поворачиваем
                self.semaphoreEn[key.split('-')[0][::-1] + '-' + key.split('-')[1][::-1]] = value

    def getSemaphoreRu(self,inputStr):
        inputStr = inputStr.lower()
        outputStr = ''

        numFlag = False # flag for numbers that follow
        for flagCode in inputStr.split():
            outputStr += self.semaphoreRu.get(flagCode,'?')

        return outputStr

if __name__ == '__main__':
    semaphore = SemaphoreFlagsDecoder()
    print(semaphore.getSemaphoreRu('нл-нп л-нл лн-в л-в л-н нл-нп лв-пн н-п'))
    print(semaphore.getSemaphoreRu('бред какой-то всякий 123'))
    print(len(semaphore.semaphoreRu))
    print(len(semaphore.semaphoreEn))
    print(sorted(set('бред какой-то всякий 123')))
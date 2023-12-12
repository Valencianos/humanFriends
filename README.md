Информация о проекте
Необходимо организовать систему учета для питомника в котором живут домашние и Pack animals. 

Задание 
Операционные системы и виртуализация (Linux)
1. Использование команды cat в Linux
  - Создать два текстовых файла: "Pets"(Домашние животные) и "Pack animals"(вьючные животные), используя команду `cat` в терминале Linux. В первом файле перечислить собак, кошек и хомяков. 
    Во втором — лошадей, верблюдов и ослов.
  - Объединить содержимое этих двух файлов в один и просмотреть его содержимое.
  - Переименовать получившийся файл в "Human Friends"(.


2. Работа с директориями в Linux
  - Создать новую директорию и переместить туда файл "Human Friends".


3. Работа с MySQL в Linux. “Установить MySQL на вашу вычислительную машину ”
  - Подключить дополнительный репозиторий MySQL и установить один из пакетов из этого репозитория.


4. Управление deb-пакетами
  - Установить и затем удалить deb-пакет, используя команду `dpkg`.


5. История команд в терминале Ubuntu



Объектно-ориентированное программирование 
6. Диаграмма классов
  - Создать диаграмму классов с родительским классом "Животные", и двумя подклассами: "Pets" и "Pack animals". В составы классов которых в случае Pets войдут классы: собаки, кошки, хомяки,
а в класс Pack animals войдут: Лошади, верблюды и ослы). Каждый тип животных будет характеризоваться (например, имена, даты рождения, выполняемые команды и т.д)


7. Работа с MySQL
7.1. После создания диаграммы классов в 6 пункте, в 7 пункте база данных "Human Friends" должна быть структурирована в соответствии с этой диаграммой. Например, можно создать таблицы, которые будут
соответствовать классам "Pets" и "Pack animals", и в этих таблицах будут поля, которые характеризуют каждый тип животных (например, имена, даты рождения, выполняемые команды и т.д.). 
7.2- В ранее подключенном MySQL создать базу данных с названием "Human Friends".
   ![image](https://github.com/Valencianos/humanFriends/assets/122907189/7fdc3348-456a-4b35-a68f-8fa7583d0cfd)
   - Создать таблицы, соответствующие иерархии из вашей диаграммы классов.
   ![image](https://github.com/Valencianos/humanFriends/assets/122907189/5f5f4cc9-20e4-4fd7-bfe2-612de6d8668d)
   ![image](https://github.com/Valencianos/humanFriends/assets/122907189/6aa84c21-b66d-4a1b-8292-76bda346cc7f)
   - Заполнить таблицы данными о животных, их командах и датами рождения.
   ![image](https://github.com/Valencianos/humanFriends/assets/122907189/6babb831-27bc-4be4-8b1b-f5540d758c28)
   ![image](https://github.com/Valencianos/humanFriends/assets/122907189/38da4fac-11b1-4bc8-b140-b213bc70f695)
   ![image](https://github.com/Valencianos/humanFriends/assets/122907189/98beb3f2-ca6d-4cc7-a53a-367ef7828f72)
   ![image](https://github.com/Valencianos/humanFriends/assets/122907189/7c64e50f-df79-4fef-aba8-66735af9a297)
   ![image](https://github.com/Valencianos/humanFriends/assets/122907189/31c0500c-b90d-40df-9574-a390de1bd27b)
   ![image](https://github.com/Valencianos/humanFriends/assets/122907189/10cd48cc-7d84-489d-8e0f-b0010dd7916a)
   - Удалить записи о верблюдах и объединить таблицы лошадей и ослов.
   ![image](https://github.com/Valencianos/humanFriends/assets/122907189/7c9c0c25-999b-4bb5-bb8d-391522324bae)
   - Создать новую таблицу для животных в возрасте от 1 до 3 лет и вычислить их возраст с точностью до месяца.
   ![image](https://github.com/Valencianos/humanFriends/assets/122907189/f8260ee7-c533-4b1e-8ee7-27171eac67da)
   - Объединить все созданные таблицы в одну, сохраняя информацию о принадлежности к исходным таблицам.
  ![image](https://github.com/Valencianos/humanFriends/assets/122907189/e71a0155-2867-4d81-804f-b0e824448509)

9. ООП и Java
  - Создать иерархию классов в Java, который будет повторять диаграмму классов созданную в задаче 6(Диаграмма классов) .


9. Программа-реестр домашних животных
  - Написать программу на Java, которая будет имитировать реестр домашних животных. 
Должен быть реализован следующий функционал:
9.1. Добавление нового животного
  - Реализовать функциональность для добавления новых животных в реестр.       
 Животное должно определяться в правильный класс (например, "собака", "кошка", "хомяк" и т.д.)
        

9.2. Список команд животного
  - Вывести список команд, которые может выполнять добавленное животное (например, "сидеть", "лежать").
        
9.3. Обучение новым командам
  - Добавить возможность обучать животных новым командам.
9.4 Вывести список животных по дате рождения

9.5. Навигация по меню
        - Реализовать консольный пользовательский интерфейс с меню для навигации между вышеуказанными функциями.
        
10. Счетчик животных
Создать механизм, который позволяет вывести на экран общее количество созданных животных любого типа (Как домашних, так и вьючных), то есть при создании каждого нового животного счетчик увеличивается на “1”. 


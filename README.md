EngineeringGeology

В качестве портфолио я создаю проект системы ведения архива для организаций, занимающихся инженерно-геологическими изысканиями (строительной геологией). Он включает в себя базу данных и электронные журналы буровых скважин, пользоваться которыми можно как в поле, так и в офисе. Такая система может также применяться для оцифровки существующих архивов, которые велись в аналоговой форме.

BoreLog_kivy.py (+ borelog.kv) - код мобильной версии электронного журнала для Android, которая может быть установлена на смартфоне и использоваться для полевого документирования, с возможностью сохранения информации в эксель-файле. Создано в Python с применением библиотек Kivy и OpenPyXL. 

BoreLog_cons.py - консольная версия электронного журнала, с возможностью сохранения информации в эксель-файле (разделитель - "двоеточие"). BoreLog_read.py - код для чтения введённых данных через консоль. Данная версия может использоваться как на смартфонах, оснашённых программами для работы с консолью (например, Pydroid), так и на компьютерах.

GeoBore_1.0 - код десктопной версии электронного журнала. Он может использоваться для камерального документирования и поддерживает возможность поиска, редактирования и удаления информации. Создано в Python с применением библиотек Tkinter и SQLite3, а также СУБД SQLite. 

База данных построена в СУБД MySQL. Представлены логическая схема и скрипт. В схеме показана взаимосвязь между различными компонентами системы изысканий. База данных учитывает связи "многие ко многим" - например, в одной буровой скважине может быть несколько разных инженерно-геологических элементов (слоёв грунта), а один элемент может присутствовать в нескольких скважинах. Я постарался довести базу до третьей нормальной формы - это значит, к примеру, что я не стал разделять свойств грунта на отдельные таблицы физических и физико-механических свойств, посчитав это неудобным в использовании, однако по желанию пользователей подобные разделения могут быть осуществлены.

Актуальность решения проблемы оцифровки архива и выбора параметров фиксирующейся информации известна мне по 11 годам работы в одной из организаций данного рода деятельности. Ранее подобная работа велась в бумажном виде с дополнением в виде таблиц Excel.

Я продолжаю совершенствовать представленный проект и на нынешнем этапе занимаюсь системной интеграцией систем управления базой данных с мобильного и десктопного журналов. В дальнейшем я планирую заняться созданием конструктора чертежа скважин, создав альтернативу AutoCAD и других САПР.

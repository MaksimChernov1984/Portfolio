f = open('BoreLogCol.xls', 'a')
f.write('N объекта: N скв.: Дата: Абс.отм.: Глуб.скв.: Глуб.кровли: Описание: Вид обр.: Глуб.обр.: Глуб.подошвы\n')
print('Электронный журнал')
obj_nm = input('N объекта: ')
bore_nm = input('N скважины: ')
bore_date = input('Дата: ')
bore_abs = input('Абс.отм.: ')
bore_depth = input('Глуб.скв.: ')
layer_roof = input('Кровля ИГЭ: ')
layer_descr = input('Описание ИГЭ: ')
sample_type = input('Вид образца: ')
sample_depth = input('Глуб.образца: ')
f.write(obj_nm+':'+bore_nm+':'+bore_date+':'+bore_abs+':'+bore_depth+':'+layer_roof+':'+layer_descr+':'+sample_type+':'+sample_depth)
sample_plus = input('Ещё образец? д/н: ')
while sample_plus != 'н':
	sample_type = input('Вид образца: ')
	sample_depth = input('Глуб.образца: ')
	f.write('\n:::::::'+sample_type+':'+sample_depth)
	sample_plus = input('Ещё образец? д/н ')
layer_base = input('Подошва ИГЭ: ')
f.write(':'+layer_base+'\n')
while bore_depth != layer_base:
	layer_roof = input('Кровля ИГЭ: ')
	layer_descr = input('Описание ИГЭ: ')
	sample_type = input('Вид образца: ')
	sample_depth = input('Глуб.образца: ')
	f.write(':::::'+layer_roof+':'+layer_descr+':'+sample_type+':'+sample_depth)
	sample_plus = input('Ещё образец? д/н: ')
	while sample_plus != 'н':
		sample_type = input('Вид образца: ')
		sample_depth = input('Глуб.образца: ')
		f.write('\n:::::::'+sample_type+':'+sample_depth)
		sample_plus = input('Ещё образец? д/н ')
	layer_base = input('Подошва ИГЭ: ')
	f.write(':'+layer_base+'\n')
f.close()
ќтчЄт о тестировании яндекс ѕрилавка

“естирование API яндекс ѕрилавка проводилось с использованием инструмента Postman.
1. ƒл€ тестировани€ API составлен чек-лист, результаты тестов отмечены в нем же:
„ек-лист тестировани€ API приложени€ яндекс ѕрилавок

 оллекци€ Postman (содержит как запросы по тестированию, так и запросы дл€ локализации бага в задании 3): яндексѕрилавок.postman_collection.json


2. »з 52 успешно прошло 25, не прошло Ч 25, пропущены из-за св€занных багов - 2.
—писок багов, найденных при тестировании, разбит по приоритетам:
	Ѕлокирующие:  -
	
	 ритичные: 
	https://ilbina.youtrack.cloud/issue/107-1/Pri-zaprose-fast-delivery-v3.1.1-calculate-delivery.xml-s-parametrom-deliveryTime06-deliveryTime-v-otvete-otsutstvuet-parametr
	
	https://ilbina.youtrack.cloud/issue/107-2/Pri-zaprose-fast-delivery-v3.1.1-calculate-delivery.xml-s-parametrom-deliveryTime22-deliveryTime-v-otvete-otsutstvuet-parametr
	
	https://ilbina.youtrack.cloud/issue/107-3/Pri-otpravke-zaprosa-fast-delivery-v3.1.1-calculate-delivery.xml-s-pustym-parametrom-deliveryTime-prihodit-otvet-s-kodom-200
	
	https://ilbina.youtrack.cloud/issue/107-9/Pri-otpravke-zaprosa-DELETE-api-v1-orders-id-c-sushestvuyushim-id-korziny-prihodit-oshibka-s-kodom-404
	
	https://ilbina.youtrack.cloud/issue/107-26/Pri-otpravke-zaprosa-PUT-api-v1-orders-id-s-pustym-parametrom-productsList-v-otvete-prihodit-kod-200
	
	https://ilbina.youtrack.cloud/issue/107-17/Pri-otpravke-zaprosa-fast-delivery-v3.1.1-calculate-delivery.xml-s-pustym-parametrom-productsCount-prihodit-otvet-s-kodom-200
	
	https://ilbina.youtrack.cloud/issue/107-19/Pri-otpravke-zaprosa-fast-delivery-v3.1.1-calculate-delivery.xml-s-pustym-znacheniem-parametra-productsWeight-prihodit-otvet-s
	
	https://ilbina.youtrack.cloud/issue/107-13/Pri-otpravke-zaprosa-PUT-api-v1-orders-id-c-otricatelnym-znacheniem-kolichestva-tovara-prihodit-otvet-s-kodom-200-uspeshnaya
	
	https://ilbina.youtrack.cloud/issue/107-23/Pri-otpravke-zaprosa-PUT-api-v1-orders-id-c-pustym-znacheniem-v-kolichestve-tovara-prihodit-otvet-s-kodom-200
	

	—редний приоритет: 
	
	https://ilbina.youtrack.cloud/issue/107-21/Pri-otpravke-zaprosa-fast-delivery-v3.1.1-calculate-delivery.xml-s-otricatelnym-parametrom-productsWeight-prihodit-otvet-s-kodom
	
	https://ilbina.youtrack.cloud/issue/107-12/Pri-otpravke-zaprosa-PUT-api-v1-orders-id-c-otricatelnym-znacheniem-id-tovara-prihodit-otvet-s-kodom-409
	
	https://ilbina.youtrack.cloud/issue/107-25/Pri-otpravke-zaprosa-PUT-api-v1-orders-id-s-pustym-id-tovara-prihodit-otvet-s-kodom-500
	
	
	https://ilbina.youtrack.cloud/issue/107-22/Pri-otpravke-zaprosa-PUT-api-v1-orders-id-co-specsimvolami-v-kolichestve-tovara-prihodit-otvet-s-kodom-200
	
	https://ilbina.youtrack.cloud/issue/107-16/Pri-otpravke-zaprosa-fast-delivery-v3.1.1-calculate-delivery.xml-s-otsutstviem-parametra-deliveryTime-prihodit-otvet-s-kodom-500
	
	https://ilbina.youtrack.cloud/issue/107-15/Pri-otpravke-zaprosa-fast-delivery-v3.1.1-calculate-delivery.xml-s-bolshim-chislom-v-parametre-deliveryTime-prihodit-otvet-s
	
	https://ilbina.youtrack.cloud/issue/107-4/Pri-otpravke-zaprosa-fast-delivery-v3.1.1-calculate-delivery.xml-s-bukvami-v-znachenii-parametra-deliveryTime-prihodit-otvet-s 
	https://ilbina.youtrack.cloud/issue/107-5/Pri-otpravke-zaprosa-fast-delivery-v3.1.1-calculate-delivery.xml-s-otricatelnym-znacheniem-parametra-deliveryTime-prihodit-otvet
	
	https://ilbina.youtrack.cloud/issue/107-7/Pri-otpravke-zaprosa-fast-delivery-v3.1.1-calculate-delivery.xml-s-otsutstviem-parametra-productsCount-prihodit-otvet-s-kodom
	
	https://ilbina.youtrack.cloud/issue/107-6/Pri-otpravke-zaprosa-fast-delivery-v3.1.1-calculate-delivery.xml-s-bukvami-v-znachenii-parametra-productsCount-prihodit-otvet-s 
	https://ilbina.youtrack.cloud/issue/107-18/Pri-otpravke-zaprosa-fast-delivery-v3.1.1-calculate-delivery.xml-s-otricatelnym-chislom-v-parametre-productsCount-prihodit-otvet
	
	https://ilbina.youtrack.cloud/issue/107-20/Pri-otpravke-zaprosa-fast-delivery-v3.1.1-calculate-delivery.xml-s-otsutstviem-parametra-productsWeight-prihodit-otvet-s-kodom
	
	https://ilbina.youtrack.cloud/issue/107-10/Pri-otpravke-zaprosa-fast-delivery-v3.1.1-calculate-delivery.xml-s-bukvami-v-znachenii-parametra-productsWeight-prihodit-otvet-s
	https://ilbina.youtrack.cloud/issue/107-27/Pri-otpravke-zaprosa-POST-fast-delivery-v3.1.1-calculate-delivery.xml-s-telom-v-formate-json-prihodit-otvet-s-kodom-500
	
	https://ilbina.youtrack.cloud/issue/107-24/Pri-otpravke-zaprosa-PUT-api-v1-orders-id-co-specsimvolami-v-id-tovara-
	prihodit-otvet-s-kodom-500
	
	Ќизкий приоритет: -
	Ќезначительные:  -

?
3. ƒл€ анализа информационных логов необходимо выполнить следующие команды:

ssh 97afa4f6-c12b-4d6c-9f97-09b3ed62eaaa@serverhub.praktikum-services.ru -p 4554 - подключение к серверу

mkdir generallogs - создание папки УgenerallogsФ
cd generallogs - переход в папку УgenerallogsФ дл€ дальнейшего копировани€ файлов в нее
cp //var/www/backend/packages/main/logs/combined.log logs1.log - копирование файла с логами Уcombined.logФ из папки var/www/backend/packages/main/logs с переименованием в Уlogs1.logФ
cp //var/www/backend/packages/secondary/build/logs/combined.log logs2.log  - копирование файла с логами Уcombined.logФ из папки var/www/backend/packages/secondary/build/logs с переименованием в Уlogs2.logФ
touch info.log - создание файла  дл€ копировани€ в них нужных логов
grep -R INFO ~/generallogs > info.log - копирование информационных логов путем фильтрации строк  содержащих текст УINFOФ в файлах внутри папки УgenerallogsФ и копированием их в файл Уinfo.logФ
cat info.log - вывод содержимого файла Уinfo.logФ:

/home/morty/generallogs/logs1.log:2023-07-26T04:30:32.798Z [INFO] [Main]: Server is listening at port 4000
/home/morty/generallogs/logs1.log:2023-07-26T04:30:32.831Z [INFO] [Main]: [SOAP Client] Soap is listening at /api/wsdl
/home/morty/generallogs/logs1.log:2023-07-26T04:30:32.958Z [INFO] [Main]: [PostgreSQL] PostgreSQL is initialized
/home/morty/generallogs/logs2.log:2023-07-26T04:30:14.534Z [INFO] [Warehouse][we-have-everything]:
/home/morty/generallogs/logs2.log:2023-07-26T04:30:14.543Z [INFO] [Warehouse][we-have-everything]: Server is listening at port 4021
/home/morty/generallogs/logs2.log:2023-07-26T04:30:15.561Z [INFO] [Warehouse][attic]:
/home/morty/generallogs/logs2.log:2023-07-26T04:30:15.567Z [INFO] [Warehouse][attic]: Server is listening at port 4022
/home/morty/generallogs/logs2.log:2023-07-26T04:30:16.632Z [INFO] [Warehouse][big-world]:
/home/morty/generallogs/logs2.log:2023-07-26T04:30:16.638Z [INFO] [Warehouse][big-world]: Server is listening at port 4023
/home/morty/generallogs/logs2.log:2023-07-26T04:30:16.648Z [INFO] [Warehouse][big-world]: [SOAP Client] Soap is listening at /big-world/wsdl
/home/morty/generallogs/logs2.log:2023-07-26T04:30:17.661Z [INFO] [Warehouse][swedish-house]:
/home/morty/generallogs/logs2.log:2023-07-26T04:30:17.667Z [INFO] [Warehouse][swedish-house]: Server is listening at port 4024
/home/morty/generallogs/logs2.log:2023-07-26T04:30:18.659Z [INFO] [Courier][moscow-delivery]:
/home/morty/generallogs/logs2.log:2023-07-26T04:30:18.664Z [INFO] [Courier][moscow-delivery]: Server is listening at port 4031
/home/morty/generallogs/logs2.log:2023-07-26T04:30:19.745Z [INFO] [Courier][fast-delivery]:
/home/morty/generallogs/logs2.log:2023-07-26T04:30:19.751Z [INFO] [Courier][fast-delivery]: Server is listening at port 4032
/home/morty/generallogs/logs2.log:2023-07-26T04:30:20.655Z [INFO] [Courier][train-noises]:
/home/morty/generallogs/logs2.log:2023-07-26T04:30:20.735Z [INFO] [Courier][train-noises]: Server is listening at port 4033
/home/morty/generallogs/logs2.log:2023-07-26T04:30:20.746Z [INFO] [Courier][train-noises]: [SOAP Client] Soap is listening at /train-noises/wsdl
/home/morty/generallogs/logs2.log:2023-07-26T04:30:21.550Z [INFO] [Courier][on-a-broomstick]:
/home/morty/generallogs/logs2.log:2023-07-26T04:30:21.557Z [INFO] [Courier][on-a-broomstick]: Server is listening at port 4034
morty@caf784dd81c8:~/generallogs$


Ќесмотр€ на то, что блокирующих багов не найдено, есть существенные ошибки в работе приложени€, которые приведут к отрицательному опыту пользователей и финансовой потере (заказ в нерабочее врем€ доставки, ошибки в обработке запросов с количеством товаров) а так же часто встречающиес€ ошибки сервера с кодом 500. ѕоэтому команда тестировани€ не рекомендует публикацию текущей версии јѕ» до устранени€ всех багов.



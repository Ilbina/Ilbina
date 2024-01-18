## :bookmark_tabs: Описание:

Яндекс Самокат - это сервис, который позволяет арендовать электрический самокат на несколько дней.У сервиса есть веб-приложение, мобильное приложение и API.В веб-приложении пользователь может оформить заказ на самокат и посмотреть статус доставки курьером. В мобильном приложении курьер отслеживает и выполняет заказы по доставке самокатов.

## Содержание:

1. [Отчёт о тестировании приложения “Яндекс Самокат”](#otchet)
* [Функциональное тестирование веб-приложения](#web)
* [Ретест багов в мобильном приложении](#retest)
* [Регрессионное тестирование мобильного приложения](#regress)
2. [SQL-запросы](https://github.com/Ilbina/Ilbina/blob/main/%D0%9F%D0%BE%D1%80%D1%82%D1%84%D0%BE%D0%BB%D0%B8%D0%BE%20%D0%98%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%20%D0%BF%D0%BE%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E/%D0%9F%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%20%D0%A1%D0%B0%D0%BC%D0%BE%D0%BA%D0%B0%D1%82/%D0%97%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D1%8B%20SQL%20%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%20%D0%A1%D0%B0%D0%BC%D0%BE%D0%BA%D0%B0%D1%82.txt)
3.  Автотетст: [проверка данных после создания заказа по кейсу](https://github.com/Ilbina/Ilbina/tree/main/%D0%9F%D0%BE%D1%80%D1%82%D1%84%D0%BE%D0%BB%D0%B8%D0%BE%20%D0%98%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%20%D0%BF%D0%BE%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E/%D0%9F%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%20%D0%A1%D0%B0%D0%BC%D0%BE%D0%BA%D0%B0%D1%82/%D0%90%D0%B2%D1%82%D0%BE%D1%82%D0%B5%D1%81%D1%82%20%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7)


# <a name=otchet> 1. Отчёт о тестировании приложения “Яндекс Самокат”

 <a name=web> Функциональное тестирование веб-приложения.

Приложение проверено на стенде https://640f76ed-9fbc-4e93-988e-d64ad5a748e5.serverhub.praktikum-services.ru 
Все известные требования были покрыты [чек-листом и таблицей КЭ и ГЗ](https://docs.google.com/spreadsheets/d/1QC1gC-OUF97Q-aliZO4zkELqrfIE0JCc-oxo_2CCHzQ/edit?usp=drive_link).
Результаты выполнения тестов содержатся в том же файле.

    Из 129 тест-кейсов успешно прошло 107, не прошло — 18, пропущено —  4.  
Список багов, найденных при тестировании, разбит по приоритетам:

1. Блокирующие:
	https://ilbina.youtrack.cloud/issue/IHDiplom-5/Pri-klike-Zakazat-s-obyazatelnymi-zapolnennymi-polyami-v-forme-Pro-arendu-oformlenie-zakaza-ne-proishodit

2. Критичные:
	https://ilbina.youtrack.cloud/issue/IHDiplom-4/Pri-klike-Dalee-s-pustym-polem-Adres-v-forme-Dlya-kogo-samokat-proishodit-perehod-k-forme-Pro-arendu

3. Средний приоритет:
	https://ilbina.youtrack.cloud/issue/IHDiplom-6/Pri-klike-Zakazat-s-pustym-polem-Kogda-privezti-samokat-v-forme-Pro-arendu-nichego-ne-proishodit

	https://ilbina.youtrack.cloud/issue/IHDiplom-7/Pri-klike-Zakazat-s-pustym-polem-Srok-arendy-v-forme-Pro-arendu-nichego-ne-proishodit

	https://ilbina.youtrack.cloud/issue/IHDiplom-8/V-kalendare-pri-klike-na-pole-Kogda-privesti-samokat-nedostupna-data-tekushego-dnya.

	https://ilbina.youtrack.cloud/issue/IHDiplom-9/V-kalendare-pri-klike-na-pole-Kogda-privesti-samokat-nedostupny-predshestvuyushee-daty

	https://ilbina.youtrack.cloud/issue/IHDiplom-10/V-pole-Kogda-privezti-samokat-nedostupen-ruchnoj-vvod

4. Низкий приоритет:
	https://ilbina.youtrack.cloud/issue/IHDiplom-16/Pri-pustom-vvode-v-pole-Adres-formy-Dlya-kogo-zakaz-oshibka-ne-poyavlyaetsya

	https://ilbina.youtrack.cloud/issue/IHDiplom-17/Pri-vvode-v-pole-Telefon-formy-Dlya-kogo-zakaz-nizhnej-granicy-dopustimogo-kolichestva-simvolom-poyavlyaetsya-oshibka

	https://ilbina.youtrack.cloud/issue/IHDiplom-11/Tekst-plejsholdera-v-pole-Stanciya-metro-imeet-chernyj-cvet-vmesto-serogo

	https://ilbina.youtrack.cloud/issue/IHDiplom-12/Dlya-vybrannoj-stancii-metro-v-forme-Dlya-kogo-samokat-pered-nazvaniem-ukazan-cvet-linii-metro

	https://ilbina.youtrack.cloud/issue/IHDiplom-13/Pri-vvode-v-pole-Imya-formy-Dlya-kogo-zakaz-znacheniya-s-tire-poyavlyaetsya-oshibka

	https://ilbina.youtrack.cloud/issue/IHDiplom-14/Pri-vvode-v-pole-Familiya-formy-Dlya-kogo-zakaz-bolshe-dopustimogo-kolichestva-simvolov-oshibka-ne-poyavlyaetsya

	https://ilbina.youtrack.cloud/issue/IHDiplom-15/Pri-vvode-v-pole-Adres-formy-Dlya-kogo-zakaz-verhnej-granicy-simvolov-poyavlyaetsya-oshibka

	https://ilbina.youtrack.cloud/issue/IHDiplom-18/Pri-vvode-v-pole-Telefon-formy-Dlya-kogo-zakaz-vyshe-dopustimogo-kolichestva-simvolov-13-oshibka-ne-poyavlyaetsya

	https://ilbina.youtrack.cloud/issue/IHDiplom-19/Pri-vvode-v-pole-Kommentarij-formy-Pro-arendu-vyshe-dopustimogo-kolichestva-simvolov-oshibka-ne-poyavlyaetsya

	https://ilbina.youtrack.cloud/issue/IHDiplom-20/V-pole-Kommentarij-formy-Pro-arendu-dopuskaetsya-vvod-specsimvolov

	https://ilbina.youtrack.cloud/issue/IHDiplom-21/V-pole-Kommentarij-formy-Pro-arendu-dopuskaetsya-vvod-latinskih-bukv


   Заключение:
Самый критичный из обнаруженных багов - при создании заказа! Заказ в приложении не создается, что блокирует работу приложения, т к делает невозможным его эксплуатацию. Багу присвоен статус блокирующего. Если пользователи не смогут создавать заказ - то вся работа и веб и мобильного приложения не имеет смысл.
Поэтому на данный момент функциональность не готова к релизу, пока не устранен блокирующий баг. Но до выпуска рекомендуется исправить и все остальные так как их не так много.
Так же в процессе тестирования составлен список серых зон и рекомендаций, которые так же содержаться в файле с проверками. Наиболее хитрой серой зоной показалось подтержающее окно при клике “Создать”, так как в требованиях, ни в макете о ней ни слова. Но, хорошенько подумав, я решила отнести ее к фиче, так как подтверждение заказа точно не будет лишним с учетом принятого пользовательского поведения, и я рекомендую добавить этот пункт в требования и макет.


# <a name=retest> Ретест багов в мобильном приложении

Был проверен фикс багов. Из них не исправлено - 1, исправлено — 3. 

Список багов: 

https://ilbina.youtrack.cloud/issue/retest_samokat-7/Pri-klike-na-notifikaciyu-prilozhenie-lomaetsya (не исправлен)

https://ilbina.youtrack.cloud/issue/retest_samokat-6/Ne-poyavlyaetsya-skroll-v-bloke-filtracii-po-stanciyam-esli-dobavit-bolshe-vosmi-stancij

https://ilbina.youtrack.cloud/issue/retest_samokat-8/Pri-filtracii-po-stancii-metro-ostayutsya-vse-zakazy-a-ne-tolko-dlya-vybrannoj-stancii

https://ilbina.youtrack.cloud/issue/retest_samokat-9/Vo-vkladke-Moi-otobrazhayutsya-ne-tolko-moi-zakazy-no-i-vse-prinyatye-zakazy


# <a name=regress> Регрессионное тестирование мобильного приложения по готовым тест-кейсам 

Результаты выполнения регрессионных тестов можно посмотреть здесь: https://docs.google.com/spreadsheets/d/1VlsxVmO-MQIs0wln2qO0m7G0Up0IyAiDfov92Lewm1U/edit?usp=sharing

Из 10 тестов  успешно прошло 3, не прошло — 6, пропущен — 1.
Список багов, найденных при тестировании, разбит по приоритетам (в том числе связанные баги, обнаруженные во время тестирования):

1. Блокирующие:
	https://ilbina.youtrack.cloud/issue/IHDiplom-1/Posle-prinyatiya-zakaza-u-kurera-vo-vkladke-Moi-otobrazhaetsya-dve-odinakovye-kartochki-zakaza

	https://ilbina.youtrack.cloud/issue/IHDiplom-2/Posle-klika-Prinyat-v-polnoj-kartochke-zakaza-vo-vkladke-Moi-otobrazhaetsya-odna-kartochka-prinyatogo-zakaza.

2. Критичные:
	https://ilbina.youtrack.cloud/issue/IHDiplom-3/Pri-prinyatii-otmenennogo-zakaza-prilozhenie-lomaetsya

	https://ilbina.youtrack.cloud/issue/IHDiplom-22/Pri-prinyatii-zakaza-vzyatogo-drugim-kurerom-prilozhenie-lomaetsya

	https://ilbina.youtrack.cloud/issue/IHDiplom-25/V-kartochke-zakaza-Adres-i-Nazvanie-stancii-v-vertikalnoj-orientacii-otobrazhaetsya-ne-polnostyu

3. Средний приоритет:
	https://ilbina.youtrack.cloud/issue/IHDiplom-24/U-vkladki-Moi-prisutstvuet-sinyaya-tochka-bez-prinyatyh-zakazov

	https://ilbina.youtrack.cloud/issue/IHDiplom-26/Zakaz-s-nezapolnennym-polem-Cvet-otobrazhaetsya-v-kartochke-v-grafe-Cvet-kak-pustaya-stroka

4. Низкий приоритет:
	https://ilbina.youtrack.cloud/issue/IHDiplom-23/Posle-prinyatiya-zakaza-ego-kartochka-uezzhaet-iz-spiska-Vse-s-animaciej-dvizheniya-vlevo

   Заключение:
В результате тестирования мобильного приложения обнаружено несколько блокирующих и критичных багов. К блокирующим отнесла баг с задвоением карточки заказа, так как это влияет на всю логику работы обоих приложений (и веб и мобильного). Это наиболее критичный баг, но есть и другие - без решения которых продукт выпускать нельзя. Это в первую очередь баги с “поломкой” приложения - они говорят о неустойчивости и неготовности системы. Такие ошибки не позволят полноценно пользоваться приложением, а значит реализовать его предназначение. Так же критичным отметил баг с отображением инфо в карточке заказа - так как это основополагающая информация для курьера - с ее получением точно проблем быть не должно (хотя она и отображается в горизонтальной ориентации, во время передвижения важно удобство!).

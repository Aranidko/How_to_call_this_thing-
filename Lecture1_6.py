#СИСТЕМА КОНТРОЛЯ ВЕРСИЙ



#Сохраняет истрию развития проекта
#--Можно понять и почему были внесены изменения
#--Остаётся резервная копия, которую можно восстановить в случае возникновения проблем
#Позволяет разрабатывать новые функции и не трогать рабочую версию проекта

#--Новый и непроверенный код живёт в одной ветка, а стабильная версия в другой
#Не теряет изменений товарищей по команде
#--Если Вася и Петя изменяли разные строкчи -- изменения сохранятся
#--Если Вася и Петя меняли одну и ту же строчку -- система попросит одного из них разобраться в конфликте изменеий


#GIT
#==Работает децентрализовано: измения сперва сохраняются на компе, потом только отправляются на сервер

#Основные понятия
#Репозиторий (repository) -- место хранения кода
#Удалённый репозиторий (remote r.) -- р., размещённый на сервере и доступный участникам
#Git-хостинг -- специальный сайт для размещения удалённых р.
#Коммит (commit) -- изменение в коде (небольшое)
#История коммитов -- история развития проекта с изменениями и именами изменяющих 3:13


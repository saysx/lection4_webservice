Основной концепцией гипервизора является домен.  
**Домен** - запущенная копия виртуальной машины. 
+ Если виртуальная машина перезагружается, то её домен завершается (в момент перезагрузки) и появляется новый домен. 
+ Более того, даже при миграции содержимое копируется из одного домена в другой домен. 
+ Таким образом, за время своей жизни практически все виртуальные машины оказываются по очереди в разных доменах. 
+ Xen оперирует только понятием домена, а понятие «виртуальной машины» появляется на уровне администрирования (прикладных программ, управляющих гипервизором).

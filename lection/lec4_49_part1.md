# Паравиртуализация
Паравиртуализация - техника виртуализации, при которой гостевые операционные системы подготавливаются для исполнения в виртуализированной среде, для чего их ядро незначительно модифицируется.
+ Операционная система взаимодействует с программой гипервизора, который предоставляет ей гостевой API, вместо использования напрямую таких ресурсов, как таблица страниц памяти.
+ Код, касающийся виртуализации, локализуется непосредственно в операционную систему.
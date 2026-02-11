# Qual è lo scopo del file .gitignore e quali file critici non dovrebbero mai finire su GitHub?

.gitignore è un file dove viene indicato il precorso di file e cartelle che saranno escluse automaticamente durante la fare di git add, in modo tale che in un commit il che non si vuole pubblicare non vengano pubblicati.

Si usa anche per non pubblicare nel commit i file compilati o gli ambienti virtuali che servono solamente allo sviluppatore, anche password e database non si devono inviare nella fase di commit.

Il .gitignore può anche ingorare nell fase di git add anche i file di un determinato tipo di estensione di file.

Gitignore automaticamente viene generato in ogni progetto creato con GITHUB in base al preset scelto.
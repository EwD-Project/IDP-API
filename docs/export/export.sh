#!/bin/bash

# Convert new_app_reqs.md to new_app_reqs.pdf
pandoc "new_app_reqs.md" -o "new_app_reqs.pdf" \
--pdf-engine=xelatex --template=eisvogel --listings \
-V disable-header-and-footer

# Convert Phonographemes.md to Phonographemes.pdf
pandoc "new_app/phonographemes/Phonographemes.md" -o "docs/new_app/export/Phonographemes.pdf" \
--pdf-engine=xelatex --template=eisvogel \
-V mainfont="Linux Libertine PI" \
-V sansfont="Linux Libertine PI" \
-V monofont="Linux Libertine PI" \
-V disable-header-and-footers

# Convert pg_keys.md to PG Keys.pdf
pandoc "new_app/phonographemes/pg_keys.md" -o "docs/new_app/export/PG Keys.pdf" \
--pdf-engine=xelatex --template=eisvogel \
-V mainfont="Linux Libertine PI" \
-V sansfont="Linux Libertine PI" \
-V monofont="Linux Libertine PI" \
-V disable-header-and-footers

# Convert Plano de Pesquisa.md to Plano de Pesquisa.pdf
pandoc "Plano de Pesquisa.md" -o "docs/Plano de Pesquisa.pdf" \
--pdf-engine=xelatex --template=eisvogel --listings \
-V mainfont="Linux Libertine" \
-V sansfont="DejaVu Sans" \
-V monofont="Linux Libertine Mono O" \
-V disable-header-and-footer

Quick start:
Docs iniciales: netlify images, .gitignore, index.ss/js/html README y vite.config.js
Instalar GIT (https://git-scm.com/download/win)
Instalar node (https://nodejs.org/es/download)

python3 -m ensurepip --upgrade
npm install
npm start

Netlify:
Add new site -> import -> github -> drones_sa
Functions -> environment variables -> add a variable OPENAI_API_KEY
URL: https://serene-scone-33b6a4.netlify.app/


Tuning OpenAI:
openai tools fine_tunes.prepare_data -f "drones SA".csv
openai api fine_tunes.create -t drones-SA_prepared.jsonl -m davinci --n_epochs 16 (a 4 por defecto para varios cientos).  Coste: $1.79
Created fine-tune: ft-8Q2sA66c3I5hSZPHoO9JyFgn


Cursos de Scrimba:
- Todos: https://scrimba.com/allcourses
- The Frontend Career Path: https://scrimba.com/learn/frontend
- Become a Scrimba Pro member: https://scrimba.com/pricing
04-06-48-04
04-08-44-37
davinci:ft-personal-2023-06-04-14-49-41

# Import the os package
import os

# Import the openai package
import openai

# Set openai.api_key to the OPENAI environment variable
#openai.api_key = os.environ["OPENAI"]
openai.api_key="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"
response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[{"role": "system", "content": 'Eres un asistente sarcástico'},
                        {"role": "user", "content": 'Hola, ¿cómo estás?'}
              ])
status=response["choices"][0]["finish_reason"]
respuesta = response["choices"][0]["message"]["content"]
print(respuesta)

openai.FineTuningJob.create(training_file="C:/Users/santi/OneDrive - AYUNTAMIENTO DE MURCIA/IA/drones_sa/drones_sa.json", model="gpt-3.5-turbo")
#const openai = new OpenAIApi(configuration)
#openai.File.create(
#    file=open("drones_sa_prepared.jsonl", "rb"),
#    purpose='fine-tune'
#)
# List 10 fine-tuning jobs
#listado=openai.FineTuningJob.list(limit=10)
#print(listado)

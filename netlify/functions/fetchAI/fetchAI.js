import { Configuration, OpenAIApi } from 'openai'

const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
})

const openai = new OpenAIApi(configuration)

const handler = async (event) => {
  try {
    console.log("1")
    const response = await openai.createCompletion({
        console.log(event.body)
        model: 'ft:gpt-3.5-turbo-0613:personal::7s8u5jhx',
        prompt: event.body,
        presence_penalty: 0,
        frequency_penalty: 0.3,
        max_tokens: 100,
        temperature: 0,
        stop: [' \n', '->']
    })
    console.log("2")
    console.log(response.data)

    return {
      statusCode: 200,
      /* headers: {
        "Access-Control-Allow-Origin": "*"
      },*/
      body: JSON.stringify(
        {
          reply: response.data
        }
      ),
    }
  } catch (error) {
    console.log("3")
    return { statusCode: 500, body: error.toString() }
  }
}

module.exports = { handler }

const inputPrompt = require("../models/input-prompt")
const openai = require("../config/openai")

module.exports = {
    async sendText(req,res){
        const openaiAPI = openai.configuration()
        const imputModel = new inputPrompt(req.body)
        try{
            const responsse = await openaiAPI.createCompletion(
                openai.textCompletion ("me de nomes de artigos de nodejs")
            )
            return res.status(200).json({
                sucess: true,
                data: response.data.choises[0]
            })
        } catch(error){ 
            return res.status(400).json({
            sucess: false, 
            error: error.response 
            ? error.response.data
            : "there was an issue on the server"
            })
        }
    }
}
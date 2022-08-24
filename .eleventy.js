module.exports = function(eleventyConfig){

    eleventyConfig.addPassthroughCopy('./src/assets')
    eleventyConfig.addPassthroughCopy('./src/pages')

    return{
        dir:{
            input: "src",
            output: "public"
        }
    }
}
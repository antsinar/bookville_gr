module.exports = function(eleventyConfig){

    eleventyConfig.addPassthroughCopy('./src/assets')
    eleventyConfig.addPassthroughCopy('./src/pages')
    eleventyConfig.addPassthroughCopy('./src/admin')

    return{
        dir:{
            input: "src",
            output: "public"
        }
    }
}
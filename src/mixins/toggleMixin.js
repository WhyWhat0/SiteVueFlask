export default {
    methods:{
        calculateContentHeight(ta, scanAmount) {
            var origHeight = ta.style.height,
                height = ta.offsetHeight,
                scrollHeight = ta.scrollHeight,
                overflow = ta.style.overflow;
            if (height >= scrollHeight) {
                ta.style.height = (height + scanAmount) + 'px';
                ta.style.overflow = 'hidden';
                if (scrollHeight < ta.scrollHeight) {
                    while (ta.offsetHeight >= ta.scrollHeight) {
                        ta.style.height = (height -= scanAmount) + 'px';
                    }
                    while (ta.offsetHeight < ta.scrollHeight) {
                        ta.style.height = (height++) + 'px';
                    }
                    ta.style.height = origHeight;
                    ta.style.overflow = overflow;
                    return height;
                }
            } else {
                return scrollHeight;
            }
        },
    calculateHeight() {
        var ta = document.getElementById("ta"),
            style = (window.getComputedStyle) ?
                window.getComputedStyle(ta) : ta.currentStyle,
            taLineHeight = parseInt(style.lineHeight, 10),
            taHeight = this.calculateContentHeight(ta, taLineHeight),
            numberOfLines = Math.ceil((taHeight) / taLineHeight)-2;
            ta.scrollHeight
            // console.log('numberOfLines =',numberOfLines, '\n',
            // 'taHeight =',taHeight-1,'\n',
            // 'taLineHeight =',taLineHeight,'\n',
            // '(taHeight) / taLineHeight)-1 =',(taHeight-1) / taLineHeight, Math.ceil((taHeight-1) / taLineHeight),'\n',
            // )
            return numberOfLines
        },
    } 
}

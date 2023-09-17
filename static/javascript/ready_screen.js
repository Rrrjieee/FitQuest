const timer = setInterval(() => {
    let elem        = document.getElementById("countdown_text");
    var text_num    = parseInt(elem.innerHTML);

    text_num       -= 1;
    elem.innerHTML  = text_num.toString();
    document.title  = "FitQuest: Ready in " + elem.innerHTML;
    if (text_num > 0) {
        return;
    }
    console.log("Redirecting after 0.35 seconds.")
    clearInterval(timer);
    setTimeout(() => {
        let data_elem   = document.getElementById("page_data");
        var index       = data_elem.getAttribute("data-id");

        console.log("Redirecting")
        window.location.href    = '/user_id=' + index + '/exercise'
    }, 350)
}, 1000)

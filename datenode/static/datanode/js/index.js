 function getQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null)
        return decodeURI(r[2]);
    return null;
}
var node = (function () {
    init();

    function init() {
        var name=getQueryString('name')
        var data={
            name:name
        }
        $.ajax({
            type: "GET",
            data: data,
            url:'/datenode/getNode',
            contentType:'application/json',
            success:function (res) {
               var res=JSON.parse(res)
                if(res.code==200){
                    $("#box").text('hello: '+res.data.name)
                    $("#p").hide()
                }
            },
            error:function (res) {
                $("#p").show();
            }
        })
    }
})();

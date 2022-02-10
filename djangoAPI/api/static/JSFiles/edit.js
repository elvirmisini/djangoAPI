$(".link-edit").on("click", function(e){
    e.preventDefault();
    var $this=$(this);
    let title=$this.parents(".record").find('td').eq(0).text();
    $("#formEdit input[name='title']").val(title);
    $("#formEdit").attr("action", $this.attr('href'));
    $("#editModal").modal("show");

    return false;
});
//$("#formEdit").on("submit", function(e){
// e.preventDefault();
// var $this=$(this);
//$.ajax({
//    type:'POST',
//    url:$this.attr("action"),
//    async: 'true',
//    data: {title: $('#title').val()},
//
//    success: function(data) {
//        alert(data)
//    },
//
//});
//});
//$("#formEdit").on("submit", function(e){
//e.preventDefault();
//e.stopPropagation();
//let data=$this.serialize();
//            $.ajax({
//
//            url: $this.attr("action"),
//            type: "POST",
//            data:data,
//            dataType: "json",
//            success: function(resp){
//                if(resp.message == "success"){
//                    alert("Updatet success")
//                    $("#editModal").modal("hide");
//                    };
//                }else{
//                alert(resp.message);
//                },
//                error: function(resp){
//                console.log("Something wrong")
//                }
//                }
//            }
//        });
//});
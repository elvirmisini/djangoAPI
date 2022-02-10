$(".link-delete").on("click", function(e){
    e.preventDefault();
    var $this = $(this);
    if(confirm("Sure to delete?")){
        $.ajax({
            url: $this.attr("href"),
            type: "GET",
            dataType: "json",
            success: function(resp){
                if(resp.message == "success"){
                    $this.parents(".record").fadeOut("slow", function(){
                        $this.parents(".record").remove();
                    });
                }else{
                    alert(resp.message);
                }
            }
        });
    }
    return false;
});
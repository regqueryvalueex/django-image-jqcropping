function init_croping_block(name){
    var block = $("#"+name+"-crop");
    var ratio = block.attr('data-size').split("x");
    var crop_name = block.attr('data-name').split("x");
    ratio     = parseInt(ratio[0])/parseInt(ratio[1]);
    var dataX1      = block.find("input[name="+crop_name+"_0]");
    var dataY1      = block.find("input[name="+crop_name+"_1]");
    var dataWidth   = block.find("input[name="+crop_name+"_2]");
    var dataHeight  = block.find("input[name="+crop_name+"_3]");
    var dataX2      = block.find("input[name="+crop_name+"_4]");
    var dataY2      = block.find("input[name="+crop_name+"_5]");
    var init_data = {x1:dataX1.val(), y1:dataY1.val(), x2:dataX2.val(), y2:dataY2.val(), width: dataWidth.val(), height: dataHeight.val()};
    $('#'+name+'-img-crop').html($('a[data-name='+name+'] img').clone());
    var image = $('#'+name+'-img-crop img');
    image.cropper({
                aspectRatio: ratio,
                data: init_data,
                done: function(data) {
                    dataX1.val(data.x1);
                    dataY1.val(data.y1);
                    dataX2.val(data.x2);
                    dataY2.val(data.y2);
                    dataHeight.val(data.height);
                    dataWidth.val(data.width);
                }
            });
}

$(document).ready(function() {
    var fields = $('.img-cropping');
    for(var i=0; i<fields.length; i++){
        var name = $(fields[i]).attr('name');
        var selector = '[data-name='+name+']';
        if($('a').is(selector)){
            init_croping_block(name);
        }
        else{
            $('#'+name+'-img-crop').text("Не выбрано");
        }
    }

    $('input.img-cropping').change(function(){
        var input = this;
        if (input.files && input.files[0]) {
            if ( input.files[0].type.match('image.*') ) {
                var reader = new FileReader();
                reader.onload = function(e) {
                    var name = $(input).attr('name');
                    var preview = e.target.result;
                    var selector = '[data-name='+name+']';
                    if(!$('a').is(selector)){
                        $(input).before('На данный момент: <a href="" data-name="'+name+'" class="crop-dialog-open"><img src=""/></a> <br />Изменить:');
                    }
                    $("#"+name+"-crop").find('input').val(null);
                    $('a[data-name='+name+'] img').attr('src', preview);
                    $('#'+name+'-img-crop img').cropper("disable");
                    init_croping_block(name);
                }
                reader.readAsDataURL(input.files[0]);
            } else console.log('is not image mime type');
        }
        else console.log('not isset files data or files API not supordet');
    });
});
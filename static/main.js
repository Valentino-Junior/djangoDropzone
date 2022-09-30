
// Dropzone.autoDiscover=false;
// const myDropzone= new Dropzone('#my-dropzone',{
//     url:'upload/',
//     maxFiles:5,
//     maxFilesize:2,
//     acceptedFiles:'.jpg',
// })
Dropzone.autoDiscover=true;
var myDropzone = new Dropzone("#designdocumentexcel",
{
    acceptedFiles : ".xls,.xlsx,jpg,.csv,.docs",
    init: function(){
        this.on("error", function(file, errorMessage) {
            alert("error : " + errorMessage );
        });

    },
}
);
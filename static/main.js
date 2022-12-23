
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
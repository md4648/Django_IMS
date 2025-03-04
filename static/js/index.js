$(document).ready(function(){
    $('.table').paging({limit:2});
    $(".datetimeinput").datepicker({changeYear:true,changeMonth:true, dateFormat:'yy-mm-dd'});
})
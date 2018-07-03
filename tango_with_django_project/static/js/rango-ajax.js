$(document).ready(function(){
$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/rango/like_category/', {category_id: catid}, function(data){
        $('#like_count').html(data);
        $('#likes').hide();
        });
     });
$('#suggestion').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/rango/suggest_category/', {suggestion: query}, function(data){
        $('#cats').html(data);
        });
        });

$('.add_page').click(function(){
    var pagename = $(this).attr("page_name");
    var pageurl = $(this).attr("page_url");
    var catid = $(this).attr("data-catid");
    $.get('/rango/auto_add_page/', {category_id: catid, page_name: pagename, page_url: pageurl}, function(data){
        $('#Add_page').hide();
    });
    });
     });

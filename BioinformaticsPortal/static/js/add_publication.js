function updateTypeName(select){
    let text = ['Journal Name', 'Conference Name']
    $('label[for="id_typeName"]').html(text[select.selectedIndex])
}

function addAuthor(){
    let form_idx = $('#id_form-TOTAL_FORMS').val();
	$('#author_form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx).replace('id="author_form_"',`id="author_form_${form_idx}"`).replace('onclick="removeAuthor()"',`onclick="removeAuthor(${form_idx})"`));
	$('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
}

function removeAuthor(){
    let form_idx = $('#id_form-TOTAL_FORMS').val();
    $(`#author_form_${form_idx-1}`).remove();
    $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) - 1);
}
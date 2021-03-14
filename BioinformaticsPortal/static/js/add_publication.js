function updateTypeName(select){
    let text = ['Journal Name', 'Conference Name']
    $('label[for="id_typeName"]').html(text[select.selectedIndex])
}

function addAuthor(){
    let form_idx = $('#id_form-TOTAL_FORMS').val();
	$('#author_form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx).replace('id="author_form_"',`id="author_form_${form_idx}"`).replace('onclick="removeAuthor()"',`onclick="removeAuthor(${form_idx})"`));
	$('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
}

function removeAuthor(val){
    let form_idx = $('#id_form-TOTAL_FORMS').val();
    $(`#author_form_${val}`).remove();
    //Update existing forms
    let author_forms = $(`[id^=author_form_]`);
    delete author_forms[0] //remove first item (wrapper)
    delete author_forms[author_forms.length-1] //remove last item (empty form)
    author_forms.length -= 2;

    author_forms = Object.values(author_forms).slice(0,2)
    for(let x = 0; x < author_forms.length; x++){
        author_forms[x].id = `author_form_${x}`;
        author_forms[x].innerHTML = author_forms[x].innerHTML.replace(/removeAuthor\(\d*/gm,`removeAuthor(${x}`);
        author_forms[x].innerHTML = author_forms[x].innerHTML.replace(/for="id_form-\d*/gm,`for="id_form-${x}`);
        author_forms[x].innerHTML = author_forms[x].innerHTML.replace(/id="id_form-\d*/gm,`id="id_form-${x}`);
        author_forms[x].innerHTML = author_forms[x].innerHTML.replace(/name="form-\d*/gm,`name="form-${x}`);
    }

    console.log(author_forms);
    $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) - 1);
}
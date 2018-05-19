tinymce.init({
  selector: 'textarea',
  height: 500,
  theme: 'modern',
  plugins: 'preview searchreplace visualblocks visualchars image link codesample code table hr pagebreak anchor lists textcolor wordcount colorpicker textpattern help',
  toolbar1: 'formatselect | bold italic strikethrough forecolor backcolor | link | alignleft aligncenter alignright alignjustify  | numlist bullist outdent indent  | removeformat',
  image_advtab: true,
  content_css: [
    '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
    '//www.tinymce.com/css/codepen.min.css'
  ]
 });

const ValidateInput = () => {

   let icon = document.querySelector('.input-group-text');
   let password = document.querySelector('#password');

   const show = () => {
      if (icon.classList.contains("fa-eye")) {
         password.type = 'password'
         icon.classList.replace('fa-eye', "fa-eye-slash")

      } else {
         password.type = 'text'
         icon.classList.replace('fa-eye-slash', "fa-eye")
      }
   }

   icon.addEventListener('click', show)
}

ValidateInput()
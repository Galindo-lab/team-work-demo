
new Vue({
    delimiters: ['[[', ']]'],
    el: '#Belbin',
    data: {
        // Estructura del formulario
        sections: [
            {
                title: "seccion 1",
                totalPoints: 0,
                questions: [
                    {
                        label: "pregunta 1",
                        for: "",
                        points: 0,
                    },
                ]
            },
            {
                title: "seccion 2",
                totalPoints: 0,
                questions: [
                    {
                        label: "pregunta 1",
                        for: "",
                        points: 0,
                    },
                    {
                        label: "pregunta 2",
                        for: "",
                        points: 0,
                    },
                ]
            },
            // agregar las secciones faltantes...
        ]
    },
    methods: {        
        submitForm(event) {
            // acciones cuando se presiona aceptar
            event.preventDefault();
            console.log(this.sections);
        }
    },
    watch: {

    }
})









// const csrfToken = '{{ csrf_token }}';

// const data = {
//     name: 'John Doe',
//     age: 25,
// };


// new Vue({
//     delimiters: ['[[', ']]'],
//     el: '#app',
//     data: {
//         sections: [
//             {
//                 title: 'Sección 1',
//                 questions: [
//                     { label: 'Pregunta 1', points: 0 },
//                     { label: 'Pregunta 2', points: 0 },
//                     { label: 'Pregunta 3', points: 0 },
//                     { label: 'Pregunta 4', points: 0 },
//                     { label: 'Pregunta 5', points: 0 },
//                     { label: 'Pregunta 6', points: 0 },
//                     { label: 'Pregunta 7', points: 0 },
//                     { label: 'Pregunta 8', points: 0 },
//                     { label: 'Pregunta 9', points: 0 }
//                 ],
//                 remainingPoints: 10,
//                 totalPoints: 0
//             },
//         ]
//     },
//     methods: {
//         submitForm() {
//             // Validar que la suma de los puntos sea igual a 10 en cada sección
//             for (const section of this.sections) {
//                 const sectionPoints = section.questions.reduce((sum, question) => sum + parseInt(question.points), 0);

//                 if (sectionPoints !== 10) {
//                     alert(`La suma de los puntos en la sección "${section.title}" debe ser igual a 10.`);
//                     return;
//                 }
//             }

//             // Enviar los datos del formulario
//             const formData = {
//                 sections: this.sections
//             };

//             // Aquí puedes realizar una solicitud a tu backend (por ejemplo, enviar los datos a Django)
//             console.log(formData);
//         }
//     },
//     watch: {
//         sections: {
//             handler(newSections) {
//                 for (const section of newSections) {
//                     section.remainingPoints = 10 - section.questions.reduce((sum, question) => sum + parseInt(question.points), 0);
//                     section.totalPoints = section.questions.reduce((sum, question) => sum + parseInt(question.points), 0);
//                 }
//             },
//             deep: true
//         }
//     }
// });
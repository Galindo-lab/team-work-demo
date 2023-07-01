
new Vue({
    delimiters: ['[[', ']]'],
    el: '#Belbin',
    data: {
        sections: [

            // {
            // title: "sección de ejemplo",   Titulo de la sección 
            // availablePoints: 10,           Maximo numero de puntos para repartir
            // points: 0,                     Numero de puntos repartidos
            // questions: [
            // {
            //   label: "pregunta 1",         Texto de la pregunta 
            //   points: 0,                   Numero de puntos asignados
            //   profile: "plant"             Perfil al que aportan los puntos:
            //                                 - resource_investigator
            //                                 - team_worker
            //                                 - coordinator
            //                                 - plant
            //                                 - monitor_evaluator
            //                                 - specialist
            //                                 - shaper
            //                                 - implementer
            //                                 - completer_finisher
            // },
            // ]
            // }, 

            {
                title: "seccion 1",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        label: "pregunta 1",
                        profile: "tonto",
                        points: 0,
                    },
                ]
            },

            {
                title: "seccion 2",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        label: "pregunta 1",
                        profile: "implementer",
                        points: 0,
                    },
                    {
                        label: "pregunta 2",
                        profile: "completer_finisher",
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

            for (const section of this.sections) {
                if (section.points !== section.availablePoints) {
                    // si la cantidad de puntos distribuidos es diferente
                    // a los puntos disponibles, enviar un error 
                    alert("error en la seccion " + section.title)
                    return
                }
            }

            // obtener el elemento seleccionado
            var form = event.target;

            // extraer el csrf del formulario (para las peticiones a django)
            var csrfToken = form.elements.csrfmiddlewaretoken.value;

            // convertir el formulario al modelo del 'BelbinUserProfile'
            var belbin = this.belbinProfile()

            // fetchdata
            console.log("okidoky")

        },

        belbinProfile() {
            // convierte los resultados a un modelo 'BelbinUserProfile'
            var formData = new FormData();

            // agregar los perfiles al form agrega 
            // redundiancia (la repeticion es aproposito)
            formData.append('resource_investigator', 0);
            formData.append('team_worker', 0);
            formData.append('coordinator', 0);
            formData.append('plant', 0);
            formData.append('monitor_evaluator', 0);
            formData.append('specialist', 0);
            formData.append('shaper', 0);
            formData.append('implementer', 0);
            formData.append('completer_finisher', 0);

            // lista de perfiles
            const profiles = [
                'resource_investigator',
                'team_worker',
                'coordinator',
                'plant',
                'monitor_evaluator',
                'specialist',
                'shaper',
                'implementer',
                'completer_finisher'
            ]

            for (const section of this.sections) {
                for (const question of section.questions) {

                    if (!profiles.includes(question.profile)) {
                        // si el perfil no existe se omite
                        console.log(`El perfil ${question.profile} no existe, se omitira su informacion`)
                        continue
                    }

                    // incrementar los puntos 
                    points = formData.get(question.profile) + question.points 
                    formData.set(question.profile, profilePoints)
                }
            }

        }
    },
    watch: {
        sections: {
            handler(form) {

                // actualizar los puntos en cada seccion 
                for (const section of form) {
                    section.points = section.questions.reduce((sum, question) => {
                        return sum + parseInt(question.points);
                    }, 0);
                }

            },
            deep: true
        }
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
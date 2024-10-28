/*
  | Inglés                | Español                             | Abreviación |
  |-----------------------|-------------------------------------|-------------|
  | Implementer           | Implementador                       | IMP         |
  | Coordinator           | Coordinador                         | CO          |
  | Shaper                | Impulsor                            | SH          |
  | Plant                 | Cerebro                             | PL          |
  | Completer Finisher    | Finalizador                         | CF          |
  | Monitor Evaluator     | Monitor Evaluador                   | ME          |
  | Teamworker            | Trabajador en Equipo / Cohesionador | TW          |
  | Resource Investigator | Investigador de Recursos            | RI          |
  | Specialist            | Especialista                        | SP          | 
*/

const preguntasData = {
  "sections": [
    {
      "name": "1 - ¿Qué es lo que yo creo que puedo aportar a un equipo?",
      "questions": [
        {
          "label": "Creo que sé ver rápidamente nuevas oportunidades y sacar partido de ellas.",
          "profile": "CF"
        },
        {
          "label": "Sé trabajar bien con una amplia variedad de gente.",
          "profile": "TW"
        },
        {
          "label": "Producir ideas es una de mis aptitudes personales.",
          "profile": "PL"
        },
        {
          "label": "Mi habilidad reside en ser capaz de hacer que las personas hablen cuando detecto que tienen algo de valor con lo que contribuir a los objetivos del grupo.",
          "profile": "CO"
        },
        {
          "label": "Mi efectividad personal tiene mucho que ver con mi capacidad para ‘seguir hacia delante’.",
          "profile": "RI"
        },
        {
          "label": "No me importa afrontar una impopularidad temporal si esta lleva a resultados que al final merezcan la pena.",
          "profile": "SH"
        },
        {
          "label": "Normalmente soy capaz de saber qué es realista y qué es lo que tiene posibilidades de funcionar.",
          "profile": "IM"
        },
        {
          "label": "Puedo argumentar razonadamente en favor de distintas alternativas de acción excluyentes sin que estén presentes los prejuicios.",
          "profile": "ME"
        },
        {
          "label": "Mis comentarios tanto sobre los puntos generales como específicos son siempre bien recibidos.",
          "profile": "SP"
        }
      ]
    },
    {
      "name": "2 - Si tuviera algún problemilla trabajando en equipo, podría ser debido a:",
      "questions": [
        {
          "label": "No estoy a gusto a menos que las reuniones estén bien estructuradas, controladas y generalmente bien conducidas.",
          "profile": "IM"
        },
        {
          "label": "Tengo inclinación a ser demasiado generoso hacia otros que tienen un punto de vista válido al que no se le ha prestado suficiente atención.",
          "profile": "CO"
        },
        {
          "label": "Cuando en el equipo nos ponemos a buscar nuevas ideas, yo tiendo a hablar demasiado.",
          "profile": "CF"
        },
        {
          "label": "Mi punto de vista, más objetivo, hace que me resulte difícil el reunirme cómodamente con colegas.",
          "profile": "ME"
        },
        {
          "label": "Algunas veces soy visto como enérgico y dominante si se tiene que hacer una cosa.",
          "profile": "SH"
        },
        {
          "label": "Encuentro difícil el dirigir estando al frente, quizá porque me puedo dejar llevar demasiado por el ambiente del grupo.",
          "profile": "TW"
        },
        {
          "label": "Tengo tendencia a ensimismarme en ideas que se me ocurren a mí; y por ello perder el contacto con lo que estamos haciendo.",
          "profile": "PL"
        },
        {
          "label": "Mis colegas ven que suelo estar preocupado innecesariamente por los detalles y por la posibilidad de que las cosas vayan mal.",
          "profile": "RI"
        },
        {
          "label": "Me cuesta contribuir a no ser que el tema tenga algo ver con algo que conozca bien.",
          "profile": "SP"
        }
      ]
    },
    {
      "name": "3 - Cuando estoy metido en un proyecto con otras personas:",
      "questions": [
        {
          "label": "Tengo capacidad para influir sobre las personas sin presionarlas.",
          "profile": "CO"
        },
        {
          "label": "Mi nivel de atención continua me evita el cometer tanto omisiones como errores por descuido.",
          "profile": "RI"
        },
        {
          "label": "No dudo en tomar medidas para asegurar que en la reunión no se pierde el tiempo ni se pierden de vista los objetivos.",
          "profile": "SH"
        },
        {
          "label": "Se puede contar conmigo para contribuir con algo original.",
          "profile": "PL"
        },
        {
          "label": "Estoy siempre dispuesto a respaldar una buena sugerencia de interés para todos.",
          "profile": "TW"
        },
        {
          "label": "Me gusta buscar lo último en ideas y desarrollos.",
          "profile": "CF"
        },
        {
          "label": "Creo que mi capacidad de juicio puede ayudar a tomar la decisión adecuada.",
          "profile": "ME"
        },
        {
          "label": "Se puede confiar en mí para contar con que todo el trato esencial esté organizado.",
          "profile": "IM"
        },
        {
          "label": "Se puede tener la seguridad de que seré yo mismo.",
          "profile": "SP"
        }
      ]
    },
    {
      "name": "4 - Mi forma de abordar el trabajo en equipo es:",
      "questions": [
        {
          "label": "Tengo bastante interés en conocer mejor a los colegas.",
          "profile": "TW"
        },
        {
          "label": "Soy reacio a dar una oportunidad a los puntos de vista de otros o a apoyar el punto de vista de una minoría.",
          "profile": "SH"
        },
        {
          "label": "Generalmente encuentro un argumento con el que refutar proposiciones poco firmes.",
          "profile": "ME"
        },
        {
          "label": "Creo que tengo talento para hacer que funcionen las cosas una vez tiene que ponerse en práctica un plan.",
          "profile": "IM"
        },
        {
          "label": "Tengo tendencia a evitar lo obvio y salir con lo inesperado.",
          "profile": "PL"
        },
        {
          "label": "Aporto un toque de perfección a todo el trabajo que dirijo.",
          "profile": "RI"
        },
        {
          "label": "Hago uso de contactos ajenos al grupo en sí mismo.",
          "profile": "CF"
        },
        {
          "label": "Al mismo tiempo que estoy interesado en todos los puntos de vista, no tengo ningún problema cuando la decisión ha de ser tomada.",
          "profile": "CO"
        },
        {
          "label": "Contribuyo cuando realmente sé del tema.",
          "profile": "SP"
        }
      ]
    },
    {
      "name": "5 - Obtengo satisfacción de un trabajo porque...",
      "questions": [
        {
          "label": "Disfruto analizando situaciones y sopesando las posibles alternativas.",
          "profile": "ME"
        },
        {
          "label": "Me intereso por encontrar soluciones prácticas a los problemas.",
          "profile": "IM"
        },
        {
          "label": "Me gusta ver que estoy fomentando buenas relaciones de trabajo.",
          "profile": "TW"
        },
        {
          "label": "Sé influir fuertemente en la toma de decisiones.",
          "profile": "SH"
        },
        {
          "label": "Sé contactar con gente que podría tener algo nuevo que ofrecer.",
          "profile": "CF"
        },
        {
          "label": "Sé poner a la gente de acuerdo en un camino a seguir, si es necesario.",
          "profile": "CO"
        },
        {
          "label": "Me siento en mi elemento cuando puedo dedicar toda mi atención a una tarea.",
          "profile": "RI"
        },
        {
          "label": "Me gusta encontrar un área que ensanche mi imaginación.",
          "profile": "PL"
        },
        {
          "label": "Siento que estoy utilizando mi formación y mis especiales aptitudes para sacar partido de las situaciones.",
          "profile": "SP"
        }
      ]
    },
    {
      "name": "6 - Si de repente me dan la responsabilidad de una tarea difícil, con un tiempo limitado y gente desconocida:",
      "questions": [
        {
          "label": "Me apetecería retirarme a un rincón para idear una salida al problema antes que aplicar una línea de acciones.",
          "profile": "PL"
        },
        {
          "label": "Estaría dispuesto a trabajar con la persona que me mostrara la propuesta más positiva.",
          "profile": "TW"
        },
        {
          "label": "Encontraría la manera de reducir el tamaño de la tarea discerniendo a qué aspecto contribuirán mejor los diferentes individuos.",
          "profile": "CO"
        },
        {
          "label": "Mi sentido natural de la urgencia ayudaría a asegurar que no sobrepasáramos el plazo previsto.",
          "profile": "RI"
        },
        {
          "label": "Creo que no me alteraría y mantendría mi capacidad de pensar intacta.",
          "profile": "ME"
        },
        {
          "label": "Mantendría invariables los objetivos a pesar de las presiones.",
          "profile": "IM"
        },
        {
          "label": "Llevaría de la mano al grupo si viera que no está haciendo ningún progreso.",
          "profile": "SH"
        },
        {
          "label": "Fomentaría discusiones de cara a estimular nuevas ideas y hacer que algo empezara a moverse.",
          "profile": "CF"
        },
        {
          "label": "Enfocaría todo el problema desde el punto de vista del conocimiento que tuviera sobre el tema.",
          "profile": "SP"
        }
      ]
    },
    {
      "name": "7 - Haciendo referencia a los problemas que tengo trabajando en equipo:",
      "questions": [
        {
          "label": "Suelo mostrar mi impaciencia con aquellos que están impidiendo el progresar.",
          "profile": "SH"
        },
        {
          "label": "Los demás podrían criticarme por ser demasiado analítico e insuficientemente intuitivo.",
          "profile": "ME"
        },
        {
          "label": "Mi deseo de asegurar que el trabajo se hace de manera adecuada puede suponer un freno.",
          "profile": "RI"
        },
        {
          "label": "Tiendo a aburrirme bastante fácilmente y a confiar en uno o dos miembros del grupo interesantes para sacarme del aburrimiento.",
          "profile": "CF"
        },
        {
          "label": "Encuentro difícil empezar algo a no ser que las metas estén claras.",
          "profile": "IM"
        },
        {
          "label": "A veces soy pobre en la explicación y clarificación de ideas complejas que se me ocurren a mí.",
          "profile": "PL"
        },
        {
          "label": "Soy consciente de que pido a los otros las cosas que no puedo hacer por mí mismo.",
          "profile": "CO"
        },
        {
          "label": "Dudo en exponer mis puntos de vista cuando me encuentro con una buena oposición.",
          "profile": "TW"
        },
        {
          "label": "Me inclino a pensar que estoy perdiendo el tiempo y que lo haría mejor yo solo.",
          "profile": "SP"
        }
      ]
    }          
  ]
}
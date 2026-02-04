from presentation.executive_summary import (
    executive_summary,
    generar_presentacion_ejecutiva,
)

slides = generar_presentacion_ejecutiva(executive_summary)

print("\nSlides generados:\n")

for slide in slides:
    print(f"- {slide['titulo']}")

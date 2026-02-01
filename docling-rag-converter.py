import logging
import sys
from pathlib import Path
from docling.document_converter import DocumentConverter

# --- Konfiguráció ---
INPUT_DIR = Path("./input")
OUTPUT_DIR = Path("./output")

# Támogatott fájltípusok (bővíthető)
VALID_EXTENSIONS = {".pdf", ".docx", ".xlsx", ".html", ".pptx"}

def setup_logging():
    """Logolás beállítása, hogy lássuk mi történik."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    return logging.getLogger("RAG-Converter")

def main():
    logger = setup_logging()
    
    # 1. Mappák ellenőrzése
    if not INPUT_DIR.exists():
        INPUT_DIR.mkdir(parents=True)
        logger.warning(f"⚠️  Létrehoztam az '{INPUT_DIR}' mappát.")
        logger.warning("👉 Kérlek másold ide a feldolgozandó fájlokat, majd futtasd újra a scriptet!")
        return

    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True)
        logger.info(f"📁 Kimeneti mappa létrehozva: {OUTPUT_DIR}")

    # 2. Fájlok összegyűjtése
    files = [f for f in INPUT_DIR.iterdir() if f.suffix.lower() in VALID_EXTENSIONS]
    
    if not files:
        logger.warning(f"⚠️  Az '{INPUT_DIR}' mappa üres vagy nem tartalmaz támogatott fájlokat.")
        logger.info(f"ℹ️  Támogatott kiterjesztések: {', '.join(VALID_EXTENSIONS)}")
        return

    # 3. Docling indítása
    logger.info("🚀 Docling konverter inicializálása (ez első alkalommal picit lassabb lehet)...")
    try:
        converter = DocumentConverter()
    except Exception as e:
        logger.error(f"❌ Hiba a Docling betöltésekor: {e}")
        return

    logger.info(f"📄 {len(files)} dokumentum feldolgozása indult.")

    # 4. Feldolgozás
    success_count = 0
    
    for i, file_path in enumerate(files, 1):
        try:
            logger.info(f"[{i}/{len(files)}] Feldolgozás: {file_path.name}...")
            
            # Konvertálás
            result = converter.convert(file_path)
            
            # Exportálás Markdown-ba
            markdown_content = result.document.export_to_markdown()
            
            # Mentés
            output_filename = file_path.stem + ".md"
            output_path = OUTPUT_DIR / output_filename
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(markdown_content)
                
            logger.info(f"✅ SIKER: {output_filename} elmentve.")
            success_count += 1
            
        except Exception as e:
            logger.error(f"❌ HIBA a(z) {file_path.name} fájlnál: {e}")

    # 5. Összegzés
    logger.info("-" * 30)
    logger.info(f"🏁 Feldolgozás befejezve. Sikeres: {success_count}/{len(files)}")
    if success_count > 0:
        logger.info(f"👉 A Markdown fájlokat itt találod: {OUTPUT_DIR.absolute()}")
        logger.info("💡 Tipp: Töltsd fel ezeket az Azure Storage Account-ra az AI Search indexeléshez!")

if __name__ == "__main__":
    main()

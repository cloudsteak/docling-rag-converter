# Docling RAG Konverter 🚀

Egyszerű és hatékony eszköz dokumentumok előkészítésére RAG (Retrieval-Augmented Generation) rendszerekhez (például Azure OpenAI + Azure AI Search).

A "statikus" formátumokat (PDF, DOCX, XLSX, HTML) strukturált, szemantikus **Markdown** formátumba alakítja, amit a nagy nyelvi modellek sokkal jobban értenek.

## Miért használd?

A hagyományos fájldarabolók gyakran szétrombolják a táblázatokat és elrendezési struktúrákat, ami "szemét be, szemét ki" eredményt ad RAG rendszerekben.
A **Docling** érti a dokumentumok szerkezetét, megőrzi a táblázatokat és címsorokat.

Ez az eszköz tökéletes, ha **Azure OpenAI Foundry** megoldást építesz:
1. Alakítsd át a nyers fájlokat helyileg ezzel az eszközzel.
2. Töltsd fel az elkészült `.md` fájlokat az Azure Storage Account-odba.
3. Indexeld őket Azure AI Search segítségével.
4. Élvezd a pontosabb és jobb válaszokat a csevegő modelledtől.

## Előfeltételek

- **Python 3.10+**
- **uv** (Egy rendkívül gyors Python csomagkezelő)

### Az uv telepítése

Ha még nincs telepítve az `uv`:

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

```

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

```

## Használat

Nem kell manuálisan virtuális környezetet létrehozni. Az `uv` mindent kezel.

1. **Klónozd le a repository-t:**
```bash
git clone https://github.com/cloudsteak/docling-rag-converter.git
cd docling-rag-converter

```


2. **Futtasd a konvertert:**
```bash
uv run docling-rag-converter.py

```


3. **Munkafolyamat:**
* Első futtatáskor létrehozza az `input` és `output` mappákat.
* Helyezd a fájljaidat (PDF, Word, Excel) az `input` mappába.
* Futtasd újra a parancsot: `uv run docling-rag-converter.py`
* Gyűjtsd össze a tiszta Markdown fájlokat az `output` mappából.



## Támogatott formátumok

* PDF (`.pdf`) - *elrendezés-elemzéssel és OCR-rel*
* Word (`.docx`)
* Excel (`.xlsx`)
* PowerPoint (`.pptx`)
* HTML (`.html`)

## Licenc

MIT License


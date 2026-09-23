<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./docs/assets/adk_dev_logo_light.png">
  <img src="./docs/assets/adk_dev_logo_dark.png" width="150" alt="ADK DEV" loading="lazy">
</picture>

# Resources

**A shelf of study material for learning web development, kept in one place and in the order it makes sense to read it.**

<img alt="PDF" src="https://img.shields.io/badge/PDF-EC1C24?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" loading="lazy">
<img alt="Frontend" src="https://img.shields.io/badge/Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black" loading="lazy">
<img alt="Attribution" src="https://img.shields.io/badge/See-NOTICE-3DA639?style=for-the-badge" loading="lazy">

<br><br>

[![CI](https://github.com/Dileepadari/Resources/actions/workflows/ci.yml/badge.svg)](https://github.com/Dileepadari/Resources/actions/workflows/ci.yml)

</div>

---

## What this is

Reference books and notes I collected while learning frontend development,
gathered so they are in one place rather than scattered across a downloads
folder.

**None of it is my writing.** It is other people's work, kept here for personal
study. Who wrote what, and on what terms, is in [NOTICE](./NOTICE), and that
file is the important one in this repository.

## Reading order

The filenames are numbered so the shelf sorts into a sensible path rather than
alphabetically. Start with how the web works and how to track your changes,
then the languages, then what is built on top of them.

| | Topic | Pages |
|---|---|---|
| `00` | How the internet and the web actually work | 64 |
| `00` | Git | 195 |
| `01` | HTML5 | 124 |
| `02` | CSS | 244 |
| `03` | JavaScript | 490 |
| `04` | React | 110 |

Both files numbered `00` are groundwork and can be read in either order.

## Attribution

Five of the books here are from the **Notes for Professionals** series, compiled
free of charge by [GoalKicker.com](https://goalkicker.com/) from Stack Overflow
Documentation and released under Creative Commons BY-SA. The people who wrote
the text are credited in the Credits chapter at the end of each book. If they
are useful to you, they are free to download from GoalKicker directly, and
downloading them there is better than taking them from here.

The Internet and Web Technology notes are lecture notes prepared by **Rajashree
Sukla**, Lecturer in the Department of Computer Science and Engineering at **NM
Institute of Engineering and Technology**. Copyright remains with the author and
the institution.

Full details, including what to do if you are an author who would rather not be
hosted here, are in [NOTICE](./NOTICE).

## Why there is no LICENSE file

A licence file would say what you may do with the contents of this repository,
and that is not mine to say: almost none of it is my work. The GoalKicker books
carry CC BY-SA, the lecture notes carry the author's own copyright, and the rest
belongs to whoever wrote it.

Adding an MIT licence here would claim a right to relicense other people's
books, which would be worse than having no licence at all.

## Checking

```sh
python scripts/check.py
```

Verifies that every PDF still opens and reports a sensible page count, and that
the links in this README and in NOTICE resolve. CI runs it on every push.

A repository of binary files fails quietly: a truncated commit or a bad
Git LFS migration leaves a file that is still there, still the right size on a
listing, and no longer a readable document.

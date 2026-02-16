## CORE ARCHITECTURE COMPARISON

### CONSOLE VERSION (`console_test.py`)

```
INPUT() ──▶ game_start()
              │
              ▼
         game_middle()
              │
      (while loop)
              │
              ▼
      alternate_turns()
              │
      (nested while)
              │
              ▼
        print() output
```

**Schema**

* **Execution model:** continuous, blocking loop
* **State:** live Python objects in memory
* **Control flow:** recursive + nested loops
* **I/O:** synchronous terminal input/output
* **End condition:** loop exits → process ends

---

### WEB VERSION (Flask + sessions)

```
HTTP POST ─▶ /battle_game (route)
                │
                ▼
        init_game_state(session)
                │
                ▼
        rebuild_kaiju(session)
                │
                ▼
          run_turn()
                │
                ▼
        persist_state(session)
                │
                ▼
         redirect + render
```

**Schema**

* **Execution model:** stateless request–response
* **State:** serialized snapshots in `session`
* **Control flow:** single-step per request
* **I/O:** browser events + HTML rendering
* **End condition:** state flags, not loops

---

## KEY ARCHITECTURAL SHIFT (THE IMPORTANT PART)

| Aspect         | Console          | Web                    |
| -------------- | ---------------- | ---------------------- |
| “Loop”         | `while` loops    | **User clicks = loop** |
| State lifetime | Process memory   | Session cookie         |
| Turns          | Enforced by code | Emergent from requests |
| Output         | `print()`        | Log list → template    |
| Time           | Continuous       | Discrete frames        |

---

## ONE-LINE SUMMARY

**Console:**

> *The program runs until the game ends.*

**Web:**

> *The game exists between requests; each click advances state by one frame.*

const output = {
    hookSpecificOutput: {
        hookEventName: 'SessionStart',
        additionalContext: `Python version: ${process.version}`,
    },
}

process.stdout.write(JSON.stringify(output))
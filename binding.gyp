{
  "targets": [
    {
      "target_name": "node-linux-pam-fork",
      "cflags!": ["-fno-exceptions"],
      "cflags_cc!": ["-fno-exceptions"],
      "sources": [
        "src/index.cc",
        "src/pam_worker.cpp"
      ],
      "libraries": ["-lpam"],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      "defines": ["NAPI_DISABLE_CPP_EXCEPTIONS"],
    }
  ]
}

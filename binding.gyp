{
  'targets': [
    {
      'target_name': 'bindings',
      'sources': [
        'src/bindings.cc',
        'src/node_mpg123.cc'
      ],
      "include_dirs" : [
        '<!(node -e "require(\'nan\')")'
      ],
      "link_settings": {
        "libraries": [
          "-lmpg123"
        ]
      },
      'conditions':[
        ['OS=="win"', {
        'defines':[
          'NOMINMAX'
        ]
        }]
      ]
    }
  ]
}

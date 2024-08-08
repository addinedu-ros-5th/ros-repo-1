// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_msgs:msg/TempPose.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__TEMP_POSE__STRUCT_H_
#define ROBOT_MSGS__MSG__DETAIL__TEMP_POSE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/TempPose in the package robot_msgs.
typedef struct robot_msgs__msg__TempPose
{
  bool move_flag;
  bool rotate_flag;
  double x;
  double y;
  double theta;
} robot_msgs__msg__TempPose;

// Struct for a sequence of robot_msgs__msg__TempPose.
typedef struct robot_msgs__msg__TempPose__Sequence
{
  robot_msgs__msg__TempPose * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__msg__TempPose__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_MSGS__MSG__DETAIL__TEMP_POSE__STRUCT_H_
